from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# menu_item = MenuItem()
coffee_maker.resources(dict['latte'])
user_input = input('What would you like? (espresso/latte/cappuccino): ').lower()
print('Please insert coins')
quarters = int(input('How many quarters?: '))
dime = int(input('How many dimes?: '))
nickel = int(input('How many nickels?: '))
penny = int(input('How many pennies?: '))

if user_input == 'report':
    coffee_maker.report()
    money_machine.report()
