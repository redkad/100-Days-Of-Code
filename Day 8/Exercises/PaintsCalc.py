import math

h = int(input('Enter height of wall: '))
w = int(input('Enter width of wall: '))

def calc(height, width):
    coverage = math.ceil((height * width) / 5)
    print(f'You will need {coverage} cans of paint')

calc(h,w)