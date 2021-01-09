print('Welcome to python pizza deliveries!'.title())

size = input('What size of pizza do you want? S, M or L: ').lower()
pepperoni = input('Do you want to add a pepperoni? Y or N: ').lower()
extra_chesse = input('Do you want to add an extra cheese? Y or N: ').lower()

price = 0

if size == 's':
    price = 15
    if pepperoni == 'y':
        price += 2

elif size == 'm':
    price = 20
    if pepperoni == 'y':
        price += 3

elif size == 'l':
    price = 25
    if pepperoni == 'y':
        price += 3

else:
    print('Wrong input.')

if extra_chesse == 'y':
    price += 1

print(f'Please pay ${price}') 