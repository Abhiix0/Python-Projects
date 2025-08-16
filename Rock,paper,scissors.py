import random

options = [ "rock", "paper", "scissors" ]

while True:

    player = None
    computer = random.choice(options)


    while player not in options:
      player = input("Enter your choice (rock, paper, or scissors): ")

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose! Paper covers rock.")
        else:
            print("You win! Rock crushes scissors.")    

    elif player == "paper":
        if computer == "scissors":
            print("You lose! Scissors cut paper.")
        else:
            print("You win! Paper covers rock.")    
    elif player == "scissors":
        if computer == "rock":
            print("You lose! Rock crushes scissors.")
        else:
            print("You win! Scissors cut paper.")   

    else:
        print("you lose!")    