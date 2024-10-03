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

if user == npc:
    print("draw")
elif user == 0 and npc == 2:
    print("you win")
elif npc == 0 and user == 2:
    print("you lose")
elif user > npc:
    print("you win")
else:
    print("you lose")
