import random

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n'))

rps = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",

"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

com = random.randint(0,2)

if choice <= 2:
    print(f'You chose: {rps[choice]}')
    print(f'Computer chose: {rps[com]}')

else:
    print('Type 0, 1, or 2')

if choice == com:
    print('Draw')

elif choice > 2:
    print()

elif com == 0 and choice == 2:
    print('You lose')

elif com == 1 and choice == 0:
    print('You lose')

elif com == 2 and choice == 1:
    print('You lose')

else:
    print('You win!')


