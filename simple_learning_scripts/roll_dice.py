import random

roll = random.randint(1,6)

guess = int(input('Guess die number: \n'))

if roll == guess: 
  print('CORRECT! COMPUTER ROLLED A ' + str(roll))
else: 
  print('WRONG!! :D COMPUTER ROLLED A ' + str(roll))