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

    elif user == "rock":
        if computer == "scissors":
            print("you win")
        else:
            print("you lose")

    elif user == "paper":
        if computer == "rock":
            print("you win")
        else:
            print("you lose")

    elif user == "scissors":
        if computer == "paper":
            print("you win")
        else:
            print("you lose")
