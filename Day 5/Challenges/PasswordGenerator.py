import random

print('Welcome to the PyPassword Generator')
letters = int(input('How many letters would you like in your password? '))
symbols = int(input('How many symbols would you like? '))
num = int(input('How many numbers would you like? '))
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s''t','u','v','w','x','y','z']
special_characters = ['!','~','`','@','#','$','%','^','&','*','(',')','-',
                    '_','+','=','{','}','[',']','|','/','\\',':',';','"','<','>',',','.','?']
numbers = []

passwords = ''

for i in range(1,10):
    numbers.append(str(i))

random_char = []
for letter in range(letters):     
    caps = random.randint(0,1)
    if caps == 0:
        random_char += random.choice(alphabets).upper()
    
    else:
        random_char += random.choice(alphabets)

for symbol in range(symbols):
    random_char += random.choice(special_characters)

for number in range(num):
    random_char += random.choice(numbers)

random.shuffle(random_char)
for i in random_char:
    passwords += i
    
print(f'Here is your password: {passwords}')