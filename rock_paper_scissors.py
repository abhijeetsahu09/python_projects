# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random 
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
u_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
c_choice = random.randint(0,2)
if u_choice == 0:
  print(rock)
elif u_choice == 1:
  print(paper)
else:
  print(scissors)

print("Computer Choice:")
if c_choice == 0:
  print(rock)
elif c_choice == 1:
  print(paper)
else:
  print(scissors)

if u_choice == 0 and c_choice == 2:
  print("You win")
elif u_choice == 2 and c_choice == 0:
    print("You lose")
elif u_choice < c_choice:
    print("You lose")
elif u_choice == 2 and c_choice == 1:
    print("You win")
elif u_choice == 1 and c_choice == 0:
    print("You win")
elif u_choice == c_choice:
    print("It's a Draw")
else:
  print("Wrong Input")





