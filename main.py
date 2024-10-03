import random

options = ("rock", "paper", "scissors")
user_wins = 0
computer_wins = 0

while user_wins < 2 and computer_wins < 2:
    user = input("choose rock, paper or scissors: ").lower()

    if user not in options:
        print("sorry that's not a valid option")
    else:
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

if user_wins > computer_wins:
    print("User wins", user_wins, "out of 3 matches")
else:
    print("User loses", computer_wins, "out of 3 matches")
