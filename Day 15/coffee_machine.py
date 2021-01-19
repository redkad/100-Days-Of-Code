def coffee_type(user_choice, water, milk, coffee_left):
    if user_choice == 'espresso':
        water -= 50
        coffee_left -= 18
        milk -= 0
        return [water, milk, coffee_left]

    elif user_choice == 'latte':
        water -= 200
        coffee_left -= 24
        milk -= 150
        return [water, milk, coffee_left]

    elif user_choice == 'cappuccino':
        water -= 250
        coffee_left -= 24
        milk -= 100
        return [water, milk, coffee_left]

    else:
        print('Invalid Input')
        return [water, milk, coffee_left]


def less_resources(resource):
    if resource[0] < 0:
        print('Sorry there is not enough water')
        return True

    elif resource[1] < 0:
        print('Sorry there is not enough coffee')
        return True

    elif resource[2] < 0:
        print('Sorry there is not enough Milk')
        return True


def calculate(quarters, dime, nickel, penny):
    total_quarters = quarters * 0.25
    total_dime = dime * 0.10
    total_nickel = nickel * 0.05
    total_penny = penny * 0.01
    total_coins = total_quarters + total_dime + total_nickel + total_penny
    return total_coins


def give_balance(user_choice, total_coins):
    espresso = 1.5
    latte = 2.5
    cappuccino = 3.0

    if user_choice == 'espresso':
        if total_coins < latte:
            print('Not enough money to buy espresso. Money refunded')
            return

        else:
            balance = total_coins - espresso
            return balance

    elif user_choice == 'latte':
        if total_coins < latte:
            print('Not enough money to buy latte. Money refunded')
            return

        else:
            balance = total_coins - latte
            return balance

    elif user_choice == 'cappuccino':
        if total_coins < cappuccino:
            print('Not enough money to buy cappuccino.')
            return

        else:
            balance = total_coins - cappuccino
            return balance
    else:
        print('Invalid input')


# quarters = 0.25
#  = 0.1
#  = 0.05
#  = 0.01

def coffee():
    water_resource = 300
    milk_resource = 200
    coffee_resource = 100
    money = 0

    game_over = False
    # user_balance = 0

    while not game_over:

        user_input = input('What would you like? (espresso/latte/cappuccino): ').lower()

        if user_input == 'report':
            print(f'Water: {water_resource}ml\nMilk: {milk_resource}ml\nCoffee: {coffee_resource}g\nMoney: ${money}')

            # print(result[0], result[1], result[2])

        else:

            print('Please insert coins')
            quarters = int(input('How many quarters?: '))
            dime = int(input('How many dimes?: '))
            nickel = int(input('How many nickels?: '))
            penny = int(input('How many pennies?: '))

            user_total_balance = calculate(quarters, dime, nickel, penny)
            user_balance = give_balance(user_input, user_total_balance)

            if user_balance is not None:
                money += user_total_balance - user_balance
                print(f'Here is ${round(user_balance, 2)} in change')

                result = coffee_type(user_input, water_resource, milk_resource, coffee_resource)
                resource = less_resources(result)

                if resource:
                    game_over = True

                if user_input == 'espresso':
                    water_resource = result[0]
                    milk_resource = result[1]
                    coffee_resource = result[2]

                else:
                    water_resource = result[0]
                    milk_resource = result[1]
                    coffee_resource = result[2]

                print(f'Here is your {user_input} ☕')


coffee()
# print(water_resource, milk_resource, coffee_resource)
