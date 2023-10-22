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
# 
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

game_items = ["Rock", "Paper", "Scissors"]
game_images = [rock, paper, scissors]

my_choice = input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# print(my_choice)

my_choice_int = int(my_choice)
print("\nYou chose:\n")
print(f"\n{game_items[my_choice_int]}\n{game_images[my_choice_int]}")

# if my_choice_int == 0:
#   print(f"\nRock\n{rock}")
# elif my_choice_int == 1:
#   print(f"\nPaper\n{paper}")
# elif my_choice_int == 2:
#   print(f"\nScissors\n{scissors}")
# else:
#   print("You didn\'t type a correct answer, run the program again !!!")

computer_choice_random_int_0_2 = random.randint(0, 2)
print("\nComputer chose:\n")
print(f"\n{game_items[computer_choice_random_int_0_2]}\n{game_images[computer_choice_random_int_0_2]}")

# if computer_choice_random_int_0_2 == 0:
#   print(f"\nRock\n{rock}")
# elif computer_choice_random_int_0_2 == 1:
#   print(f"\nPaper\n{paper}")
# elif computer_choice_random_int_0_2 == 2:
#   print(f"\nScissors\n{scissors}")

computer_win = "\nYou loose !!!"
i_win = "\nYou win !!! Congratulations"

# Rock and Paper, Computer wins
if my_choice_int == 0 and computer_choice_random_int_0_2 == 1:
  print(computer_win)
# Rock and Scissors, I win  
elif my_choice_int == 0 and computer_choice_random_int_0_2 == 2:
  print(i_win)
# Paper and Rock, I win 
elif my_choice_int == 1 and computer_choice_random_int_0_2 == 0:
  print(i_win)
# Paper and Scissors, Computer wins 
elif my_choice_int == 1 and computer_choice_random_int_0_2 == 2:
  print(computer_win)
# Scissors and Rock, Computer wins 
elif my_choice_int == 2 and computer_choice_random_int_0_2 == 0:
  print(computer_win)
# Scissors and Paper, I win
elif my_choice_int == 2 and computer_choice_random_int_0_2 == 1:
  print(i_win)
  # my_choice_int == computer_choice_random_int_0_2, a draw
else:
  print("It\'s a draw, you have to play again !!!")
