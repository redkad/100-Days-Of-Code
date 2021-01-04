age = input('What is your current age?: ')
year = 90
months = 12
weeks = 52
days = 365

days_left = (year - int(age)) * days
months_left = (year - int(age)) * months
weeks_left = (year - int(age)) * weeks

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left')