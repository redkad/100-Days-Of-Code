import random
import os
from art import logo

play = True

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)

    return card

def calculate_total(cards):

    if sum(cards) > 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw 🙃'
    
    elif computer_score == 0:
        return 'Lose, opponent has BlackJack 😱'

    elif user_score == 0:
        return 'Win with a Blackjack 😎'

    elif user_score > 21:
        return 'You went over. You lose 😭'

    elif computer_score > 21:
        return 'Opponent went over. You win 😁'

    elif user_score > computer_score:
        return 'You win 😃'

    else:
        return 'You lose 😤'

def blackjack():

    game_over = False

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    user_score = calculate_total(user_cards)
    computer_score = calculate_total(computer_cards)
        


    while not game_over:




        def burst():
            if computer_score == 0 or user_score == 0 or user_score > 21:
                return True    

        print(f'    Your cards: {user_cards}, current score: {user_score}')
        print(f"    Computer's first card: {computer_cards[0]}")


        if burst():
            game_over = True
        


        else:
            draw_another = input("Type 'y' to get another card, type 'n' to pass: " )

            if draw_another == 'y':
                user_cards.append(deal_card())
                user_score = calculate_total(user_cards)

            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_total(computer_cards)

    print(f'    Your final hand: {user_cards}, final score: {user_score}')    
    print(f'    Computer\'s final hand: {computer_cards}, final score: {computer_score}')    
    print(compare(user_score, computer_score))

    

while play:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == 'n':
        play = False
    else:
        os.system('cls')
        print(logo)
        blackjack()






