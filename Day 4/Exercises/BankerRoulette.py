import random


print('Welcome to Banker Roulette - Who pays the bill?')
names = input('Enter the names seprated by a (,) to continue\n')
names = names.split(', ')
print(names)
who_pays = random.randint(0, (len(names)-1))
print(f'{names[who_pays]} is paying for the meal today')
