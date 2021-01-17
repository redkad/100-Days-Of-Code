import os
from logo import logo

def add(num1, num2):

    """Takes 2 numbers and adds them together
 
    Returns:
        result: num1 + num
    """
    return num1 + num2

def subtract(num1, num2):

    """Takes 2 numbers and subtract second number from the first
 
    Returns:
        result: num1 (operation) num
    """
    return num1 - num2

def multiply(num1, num2):

    """Takes 2 numbers and multiply them
 
    Returns:
        result: num1 (operation) num
    """
    return num1 * num2

def divide(num1, num2):

    return num1 / num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calc():
    print(logo)
    
    f_num= float(input("\nWhat's the first number?: "))
    for operation in operations:
        print(operation)

    operation_symbol = input('Pick an operation: ')
    s_num = float(input("What's the second number?: "))

    results = operations[operation_symbol]
    answer = results(f_num, s_num)

    while True:
        
        print(f'{f_num} {operation_symbol} {s_num} = {answer}')
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == 'y':
            f_num = answer
            operation_symbol = input('Pick an operation: ')
            s_num = int(input("What's the next number?: "))
            results = operations[operation_symbol]
            answer = results(f_num, s_num)

        elif choice == 'n':
            os.system('cls')
            calc()

        else:
            print('Invalid input')

calc()