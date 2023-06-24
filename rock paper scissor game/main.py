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
import sys

compchoice=["rock", "paper", "scissors"]
computer=random.choice(compchoice)

player=input("What do you choose? rock, paper, or scissors?\n")
print(f"You chose {player}")

if player!="rock" or player!="scissor" or player!="paper":
  print("INVALID INDICA")
  sys.exit()

if player=="rock":
  print(rock)
elif player=="scissors":
  print(scissors)
elif player=="paper":
  print(paper)



print(f"computer chooses {computer}")
if computer=="rock":
  print(rock)
elif computer=="scissors":
  print(scissors)
else:
  print(paper)

if(player==computer):
  print("IT'S A DRAW")



if player=="rock":
  
    if computer=="paper":
     print("COMPUTER WINS")
    elif computer=="scissors":
      print("YOU WIN")

if player=="scissors":

  if computer=="paper":
    print ("YOU WIN")
  elif computer=="rock":
    print("COMPUTER WINS")

if player=="paper":

  if computer=="rock":
    print("YOU WIN")
  elif computer=="scissors":
    print("COMPUTER WINS")



