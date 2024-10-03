import random

options = ("rock", "paper", "scissors")
user = input("choose rock, paper or scissors: ").lower()

if user not in options:
    print("sorry that's not a valid option")
else:
    computer = random.choice(options)
    print("computer:", computer)

    if user == computer:
        print ("draw")

    elif user == "rock" and computer == "scissors":
            print("you win")

    elif user == "paper" and computer == "rock":
            print("you win")

    elif user == "scissors" and computer == "paper":
            print("you win")

    else:
        print("you lose")
