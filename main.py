import random

options = ("rock", "paper", "scissors")
user_wins = 0
computer_wins = 0
round_number = 1

while True:
    print("*" * 10)
    print("ROUND", round_number)
    print("*" * 10)
    round_number += 1
    user = input("choose rock, paper or scissors: ").lower()
    if not user in options:
        print("sorry that's not a valid option")
        continue

    computer = random.choice(options)
    print("computer:", computer)

    if user == computer:
        print("draw")

    elif user == "rock" and computer == "scissors" or user == "paper" and computer == "rock" or user == "scissors" and computer == "paper":
        print("you win")
        user_wins += 1

    else:
        print("you lose")
        computer_wins += 1

    if user_wins == 2:
        print("User wins", user_wins, "out of 3 matches")
        break
    elif computer_wins == 2:
        print("User loses", computer_wins, "out of 3 matches")
        break
