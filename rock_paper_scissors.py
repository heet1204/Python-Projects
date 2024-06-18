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

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if user_choice>=3 or user_choice<0:
  print("Invalid Selection ")
else:
  print(game_images[user_choice])

  bot_choice = random.randint(0,2)
  print("Computer chose: ")
  print(game_images[bot_choice])

  if user_choice ==0 and bot_choice==2:
    print("User Wins!")
  elif user_choice ==2 and bot_choice==0:
    print("Bot Wins!")
  elif user_choice==bot_choice:
   print("Its a tie")
  elif bot_choice>user_choice:
    print("Computer Wins!")
  elif user_choice>bot_choice:
    print("User Wins!")
  else:
    print("You Entered Invalid selection")
