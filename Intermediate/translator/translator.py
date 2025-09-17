import os
import sys
import time
import queue
import json
import argparse
import threading
import numpy as np

import sounddevice as sd
import vosk
from pathlib import Path
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
from pynput import keyboard

# ===================== Globals =====================
AUDIO_QUEUE = queue.Queue(maxsize=30)
LISTENING_EVENT = threading.Event()
EXIT_EVENT = threading.Event()

NOISE_THRESHOLD = 300     # ignore very quiet background sounds
TARGET_RMS = 2000         # target volume level for AGC
AGC_MAX_GAIN = 5.0        # don’t over-amplify beyond this

# ===================== Audio Callback =====================
def audio_callback(indata, frames, time_info, status):
    if status:
        print("⚠️ Audio status:", status, file=sys.stderr)

    if LISTENING_EVENT.is_set():
        audio_np = np.frombuffer(indata, dtype=np.int16).astype(np.float32)

        # Compute RMS (loudness)
        rms = np.sqrt(np.mean(audio_np**2))

        # Noise gate
        if rms < NOISE_THRESHOLD:
            return

        # Auto Gain Control (AGC)
        if rms > 0:
            gain = min(AGC_MAX_GAIN, TARGET_RMS / rms)
            audio_np = audio_np * gain

        # Clip back to int16
        audio_np = np.clip(audio_np, -32768, 32767).astype(np.int16)

        try:
            AUDIO_QUEUE.put_nowait(audio_np.tobytes())
        except queue.Full:
            pass  # drop audio if queue is full


# ===================== TTS =====================
def speak_text(text: str, lang: str = "te"):
    try:
        if not text.strip():
            return
        tts = gTTS(text, lang=lang)
        filename = "translation_out.mp3"
        tts.save(filename)

        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()
        os.remove(filename)

    except Exception as e:
        print("TTS error:", e)


# ===================== Keyboard =====================
def on_press(key):
    if key == keyboard.Key.space:
        if LISTENING_EVENT.is_set():
            LISTENING_EVENT.clear()
            print("\n🛑 Stopped listening.")
        else:
            while not AUDIO_QUEUE.empty():
                AUDIO_QUEUE.get_nowait()
            LISTENING_EVENT.set()
            print("\n🎤 Started listening... (press SPACE to stop)")


# ===================== Processing =====================
def process_utterance(recognizer, translator, target_lang):
    try:
        result = json.loads(recognizer.FinalResult())
        text = result.get("text", "").strip()
    except Exception:
        text = ""

    if not text:
        print("⚠️ No speech detected.")
        return

    print("\n📝 English transcription:", text)
    try:
        translated = translator.translate(text)
        print("🌐 Telugu translation:", translated)
        speak_text(translated, lang=target_lang)
    except Exception as e:
        print("❌ Translation error:", e)


# ===================== Mic Test =====================
def mic_test(rate, device):
    print("🎤 Mic Test with AGC (Ctrl+C to stop)")
    try:
        with sd.InputStream(samplerate=rate, device=device, channels=1, dtype="int16") as stream:
            while True:
                data, _ = stream.read(1024)
                audio_np = np.frombuffer(data, dtype=np.int16).astype(np.float32)
                rms = np.sqrt(np.mean(audio_np**2))
                if rms > 0:
                    gain = min(AGC_MAX_GAIN, TARGET_RMS / rms)
                else:
                    gain = 1.0
                print(f"Mic RMS={int(rms)}  | Gain={gain:.2f}", end="\r")
                time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n✅ Mic test stopped.")


# ===================== List Devices =====================
def list_devices():
    print("\nAvailable audio devices:\n")
    print(sd.query_devices())


# ===================== Main =====================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models-dir", default="models")
    parser.add_argument("--model", default="vosk-model-small-en-us-0.15")
    parser.add_argument("--rate", type=int, default=16000)
    parser.add_argument("--target", default="te")  # Telugu
    parser.add_argument("--device", type=int, default=None,
                        help="Audio input device index")
    parser.add_argument("--list-devices", action="store_true",
                        help="List available audio devices and exit")
    parser.add_argument("--mic-test", action="store_true",
                        help="Run mic test with AGC instead of recognition")
    args = parser.parse_args()

    if args.list_devices:
        list_devices()
        sys.exit(0)

    if args.mic_test:
        mic_test(args.rate, args.device)
        sys.exit(0)

    model_path = Path(args.models_dir) / args.model
    if not model_path.exists():
        print("❌ Model not found at:", model_path)
        sys.exit(1)

    model = vosk.Model(str(model_path))
    translator = GoogleTranslator(source="en", target=args.target)

    kb_listener = keyboard.Listener(on_press=on_press)
    kb_listener.start()

    try:
        with sd.RawInputStream(samplerate=args.rate,
                               blocksize=4096,   # good balance for weak mics
                               dtype='int16',
                               channels=1,
                               device=args.device,
                               callback=audio_callback):
            print("✅ Ready. Press SPACE to start/stop listening. Ctrl+C to quit.")

            while not EXIT_EVENT.is_set():
                LISTENING_EVENT.wait()
                if EXIT_EVENT.is_set():
                    break

                rec = vosk.KaldiRecognizer(model, args.rate)
                print("🎙️ Listening... speak now.")

                while LISTENING_EVENT.is_set() and not EXIT_EVENT.is_set():
                    try:
                        data = AUDIO_QUEUE.get(timeout=0.5)
                    except queue.Empty:
                        continue

                    if rec.AcceptWaveform(data):
                        pass

                process_utterance(rec, translator, args.target)

    except KeyboardInterrupt:
        print("\n👋 Exiting.")
    except Exception as e:
        print("❌ Audio stream error:", e)
    finally:
        EXIT_EVENT.set()
        kb_listener.stop()
        pygame.mixer.quit()


if __name__ == "__main__":
    main()
