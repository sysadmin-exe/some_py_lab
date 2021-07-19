import random

comp_choice = random.choice(['scissors', 'rock', 'paper'])

user_choice = input('Do you want - rock, paper, scissors?\n')

if comp_choice == user_choice:
  print('ITS A TIE')
elif user_choice == 'rock' and comp_choice == 'scissors':
  print('YOU WIN!!  COMPUTER CHOSE ' + comp_choice)
elif user_choice == 'paper' and comp_choice == 'rock':
  print('YOU WIN!! COMPUTER CHOSE ' + comp_choice)
elif user_choice == 'scissors' and comp_choice == 'paper':
  print('YOU WIN!! COMPUTER CHOSE ' + comp_choice)
else:
  print('YOU LOSE :( COMP WINS!! :D COMPUTER CHOSE ' + comp_choice)