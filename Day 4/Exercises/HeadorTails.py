import random

answer = 'y'

while answer == 'y':
    
    choice = input('Heads or Tails: ').lower()
    decision = random.randint(0,1)

    if decision == 0:
        print('Heads')

    elif decision == 1:
        print('Tails')

    else:
        print('Wrong Input')

    answer = input('Do you want to quit? Y or N: ').lower()
