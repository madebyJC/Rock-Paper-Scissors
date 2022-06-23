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

player = str(input("What do you choose? Type '0' for Rock, '1' for Paper, and '2' for Scissors. "))
bot = str(random.randint(0, 2))

if player == "0" and bot == "0":
  print(rock + "\n")
  print(f"Computer chose: \n {rock}")
  print("Draw!")
elif player == "0" and bot == "1":
  print(rock + "\n")
  print(f"Computer chose: \n {paper}")
  print("You Lose!")
elif player == "0" and bot == "2":
  print(rock + "\n")
  print(f"Computer chose: \n {scissors}")
  print("You Win!")
elif player == "1" and bot == "0":
  print(paper + "\n")
  print(f"Computer chose: \n {rock}")
  print("You Win!")
elif player == "1" and bot == "1":
  print(paper + "\n")
  print(f"Computer chose: \n {paper}")
  print("Draw!")
elif player == "1" and bot == "2":
  print(paper + "\n")
  print(f"Computer chose: \n {scissors}")
  print("You Lose!")
elif player == "2" and bot == "0":
  print(scissors + "\n")
  print(f"Computer chose: \n {rock}")
  print("You Lose!")
elif player == "2" and bot == "1":
  print(scissors + "\n")
  print(f"Computer chose: \n {paper}")
  print("You Win!")
elif player == "2" and bot == "2":
  print(scissors + "\n")
  print(f"Computer chose: \n {scissors}")
  print("Draw!")
else:
  print("Invalid Input!")

# OR

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")