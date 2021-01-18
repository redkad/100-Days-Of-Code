import random
import art

print(art.logo)
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

new_level = 0

game_over = False

def difficulty(level):
    if level == 'easy':
        return 10

    elif level == 'hard':
        return 5
    
new_level = difficulty(level)
print(f'You have {new_level} attempts remaining to guess the number')
guess = int(input('Make a guess: '))


def gen_number():
    number = random.randint(2, 99)
    return number

generated_number = gen_number()

def compare(num):

    global new_level
    
    if num > generated_number:
        new_level -= 1
        return 'Too high'
    elif num < generated_number:
        new_level -= 1
        return 'Too low'        
    else:
        global game_over
        game_over = True
        return f'You got it! The answer was {generated_number}'

while new_level != 0 and game_over == False:
    print(compare(guess))
    if not game_over and new_level != 0:
        print('Guess again')
        print(f'You have {new_level} attempts remaining to guess the number')
        guess = int(input('Make a guess: '))

    elif new_level == 0:
        print("You've run out of guesses, you lose")


    

