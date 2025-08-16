import random

words = ["python", "hangman", "programming", "challenge", "computer"]

stages = [
    """
     -----
     |   |
     |   O
     |  /|\\
     |  / \\
     |
    """,
    """
     -----
     |   |
     |   O
     |  /|\\
     |  / 
     |
    """,
    """
     -----
     |   |
     |   O
     |  /|\\
     |  
     |
    """,
    """
     -----
     |   |
     |   O
     |  /|
     |
     |
    """,
    """
     -----
     |   |
     |   O
     |   |
     |
     |
    """,
    """
     -----
     |   |
     |   O
     |
     |
     |
    """,
    """
     -----
     |   |
     |
     |
     |
    """
]

def choose_word():
    return random.choice(words)

def show_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print(stages[6 - attempts])
        print("Word:", show_word(word, guessed))
        print("Attempts left:", attempts)

        guess = input("Guess a letter or the whole word: ").lower()

        # ✅ Whole word guess
        if len(guess) > 1:
            if guess == word:
                print("You win! The word was:", word)
                return
            else:
                print("Wrong guess for the word!")
                attempts -= 1
                continue

        # ✅ Single letter guess
        if guess in guessed:
            print("You already guessed that!")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed for letter in word):
                print("You win! The word was:", word)
                return
        else:
            print("Wrong guess!")
            attempts -= 1

    print(stages[6])
    print("Game over! The word was:", word)

hangman()
