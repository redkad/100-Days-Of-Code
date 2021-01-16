import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\'''

print('Welcome to the secret auction program.')

ended = False
auction = {}

def highest_bider(bidding_record):
    highest = 0
    name = ''
    for key in bidding_record:
        if bidding_record[key] > highest:            
            highest = bidding_record[key]
            name = key

    print(f'The winner is {name} with a bid of ${highest}')

while not ended:
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: $"))
    choice = input("Are there other bidders? Type 'yes' or 'no': ")
    auction[name] = bid

    if choice == 'no':        
        highest_bider(auction)        
        ended = True
        
    else:
        os.system('cls')