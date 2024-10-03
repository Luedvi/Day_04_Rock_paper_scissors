import random


def asking_for_input():
    options = ("rock", "paper", "scissors")
    while True:
        user_option = input("choose rock, paper or scissors: ").lower()
        if not user_option in options:
            print("sorry that's not a valid option")
        else:
            computer_option = random.choice(options)
            print("computer:", computer_option)
            return user_option, computer_option


def calculate(user, computer, user_num_wins, computer_num_wins):
    if user == computer:
        print("draw")
    elif user == "rock" and computer == "scissors" or user == "paper" and computer == "rock" or user == "scissors" and computer == "paper":
        print("you win")
        user_num_wins += 1
    else:
        print("you lose")
        computer_num_wins += 1
    return user_num_wins, computer_num_wins


def show_winner(usr_wins, comp_wins):
    if usr_wins == 2:
        print("User wins", usr_wins, "out of 3 matches")
        return False
    elif comp_wins == 2:
        print("User loses", comp_wins, "out of 3 matches")
        return False
    else:
        return True


def run_game():
    round_number = 1
    user_wins = 0
    computer_wins = 0
    keep_looping = True

    while keep_looping:
        print("*" * 10)
        print("ROUND", round_number)
        print("*" * 10)
        round_number += 1

        user_input, computer_input = asking_for_input()
        user_wins, computer_wins = calculate(user_input, computer_input, user_wins, computer_wins)
        keep_looping = show_winner(user_wins, computer_wins)


run_game()
