"""
Simulates a rock, paper, scissors game against the computer
    - Asks user for their choice
    - Randomly selects an option
    - Prints both selections and winner
"""

import random

choices = ["rock", "paper", "scissors"]

player_choice = input("We are playing rock paper scissors! What will you choose? ").lower()
computer_choice = random.choice(choices)

print(f"You did {player_choice}")
print(f"I did {computer_choice}")

if player_choice == computer_choice:
    print("Wow, it's a tie!?")
elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    print("Dang it... you win")
else:
    print("Haha you lose!")