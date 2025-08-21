import random

low = 1
high = 100
is_running = True
answer = random.randint(low, high)
guesses = 0

print(f"Welcome to the Number Guessing Game! Guess a number between {low} and {high}.")

while is_running:
    guess = input("Enter your guess ").lower().strip()
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
        elif guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {answer} correctly!")
            is_running = False
            print("Thank you for playing the Number Guessing Game!")
            print(f"You guessed the number in {guesses} attempts.")

    else:
        print("Please enter a valid number.")
        continue    

         
