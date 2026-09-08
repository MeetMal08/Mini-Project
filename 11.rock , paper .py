#Python Rock , Paper , Scissors Game

import random

option = ("rock", "paper", "scissors")
player = None
computer = random.choice(option)
running = True

while running:

    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f"player chose: {player}")
    print(f"computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (yes/no): ").lower() == "yes":
        running = False 

print("Thanks for playing!")