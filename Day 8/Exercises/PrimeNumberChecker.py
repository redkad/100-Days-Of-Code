num = int(input('Enter a number: '))

def primeNumber(number):

    isPrime = True

    for n in range(2, (number + 1)):

        if number % 2 == 0:
            isPrime = False
        
    if isPrime:
        print(f'{number} is a prime number')

    elif number == 2:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not prime number')


primeNumber(num)