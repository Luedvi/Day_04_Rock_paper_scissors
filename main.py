rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
npc=random.randint(0,2)
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if npc==user:
    print("It's a draw")
elif user==0:
    if npc==1:
        print("You lose")
    else:
        print("You win!")
elif user==1:
    if npc==2:
        print("You lose")
    else:
        print("You win!")
else:
    if npc==0:
        print("You lose")
    else:
        print("You win!")
