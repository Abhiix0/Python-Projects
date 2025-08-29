import requests
import datetime

# ✅ Your OpenWeather API Key
API_KEY = "6507cfc47dab7eb8ed076d1007c27e38"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data from OpenWeather API for a given city."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius instead of Kelvin
    }
    response = requests.get(BASE_URL, params=params)

    # Debugging: print API response if needed
    # print(response.status_code, response.json())

    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        return {
            "city": city_name,
            "temp": temp,
            "humidity": humidity,
            "condition": condition
        }
    else:
        # Return the actual error message from OpenWeather
        try:
            error_msg = response.json().get("message", "Unknown error")
        except:
            error_msg = "Unknown error"
        return {"error": error_msg}

def log_weather(result):
    """Save weather results in a log file with timestamp."""
    with open("weather_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} | {result['city']} | "
                f"{result['temp']}°C | {result['humidity']}% | {result['condition']}\n")

def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    
    if "error" not in weather:
        print(f"\n🌍 Weather in {weather['city']}:")
        print(f"🌡 Temperature: {weather['temp']}°C")
        print(f"💧 Humidity: {weather['humidity']}%")
        print(f"☁ Condition: {weather['condition'].title()}")
        
        # Bonus logging
        log_weather(weather)
        print("\n✅ Weather data saved in 'weather_log.txt'")
    else:
        print(f"❌ Error: {weather['error']}")

if __name__ == "__main__":
    main()
