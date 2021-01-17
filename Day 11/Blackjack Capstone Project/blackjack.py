import random
play = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():

    user_cards = []
    com_cards = []    

    for _ in range(2):
        user_cards.append(random.choice(cards))
        com_cards.append(random.choice(cards))

    com_first = com_cards[0]
    user_total = sum(user_cards)
    com_total = sum(com_cards)

    if user_total == 21 and len(user_cards) == 2:
        user_total = 0
    
    elif com_total == 21 and len(com_cards) == 2:
        com_total = 0

    print(f"Your cards: {user_cards}, current score: {user_total}")  
    print(f"Computer's first card: {com_first}")

    choice = input("Type 'y' to get another card, type 'n' to pass: ")

    if choice == 'y':
        user_cards.append(random.choice(cards))
        user_total = sum(user_cards)

        print(f"Your cards: {user_cards}, current score: {user_total}")
        print(f"Computer's first card: {com_first}")

    while com_total < 17:
        com_cards.append(random.choice(cards))
        com_total = sum(com_cards)
    
    

    print(f"Your final hand: {user_cards}, final score: {user_total}")  
    print(f"Computer's final hand: {com_cards}, final score: {com_total}")

    if user_total == 0 or com_total == 0 or user_total > 21:
        print("Bust")
        play = False

    if user_total <= 21 and user_total > com_total:
        print("You win! ")

    elif user_total > 21:
        print('You went over. You lose 😭')

    elif com_total > 21:
        print("You win! ")

    else:
        print("Computer wins!") 



while play:

    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    if choice == 'n':
        play = False
    
    elif choice == 'y':
        blackjack()

    else:
        print('Invalid input')