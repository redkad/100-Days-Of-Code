print('Welcome to the tip calculator.')
amount = input('What was the total bill? $')
percentage = input('What percentage tip would you like to give? 10, 12, or 15?: ')
people = input('How many people are to split the bill? ')

new_percentage = float(percentage)/100
new_amount = (float(amount) * new_percentage) + float(amount)
payable = new_amount / int(people)

print(f'Each person should pay: ${round(payable , 2)}')