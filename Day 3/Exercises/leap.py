year = input('Enter year: ')

a = int(year) 


if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print('Leap Year')
        else:
            print('Not Leap')
    else:
        print('Leap Year') 
else:
    print('Not Leap')