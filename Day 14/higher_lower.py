import game_data
import art
import random
import os

def get_data(data):
    new_data = random.choice(data)
    return new_data

def get_description(celebrity, data):
    data.clear()
    for key in celebrity:
        data.append(celebrity[key])
    return data

def compare(celeb1, celeb2):
    if celeb1 > celeb2:
        return 'A'
    else:
        return 'B'

def check_answer(user_choice, result, first_follower_data, second_follower_data, game):
    if user_choice == result:
        first_follower_data = second_follower_data
        return first_follower_data
    
    else:
        game = True
        return game

def game():
    first_follower = get_data(game_data.data)
    second_follower = get_data(game_data.data)

    if first_follower == second_follower:
        second_follower = get_data(game_data.data)

    new_data1 = []
    new_data2 = []
    score = 0

    game_over = False        
    n_data1 = get_description(first_follower, new_data1)

    n_data2 = get_description(second_follower, new_data2)


    # print()

    # print(get_data(game_data.data))
    print(art.logo)
    print(f'Compare A: {n_data1[0]}, a {n_data1[2]}, from {n_data1[3]}')
    print(art.vs)
    print(f'Compare B: {n_data2[0]}, a {n_data2[2]}, from {n_data2[3]}')
    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
    result = compare(new_data1[1], n_data2[1])


    check_answer_result = check_answer(user_input, result, first_follower, second_follower, game_over)

    while check_answer_result != True:
        first_follower = check_answer(user_input, result, first_follower, second_follower, game_over)
        
        if first_follower != True:
            score+=1
            second_follower = get_data(game_data.data)
            n_data1 = get_description(first_follower, new_data1)
            n_data2 = get_description(second_follower, new_data2)
            os.system('cls')
            print(f"You're right! Current score: {score}.")
            print(f'Compare A: {n_data1[0]}, a {n_data1[2]}, from {n_data1[3]}')
            print(art.vs)
            print(f'Compare B: {n_data2[0]}, a {n_data2[2]}, from {n_data2[3]}')

            user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
            result = compare(new_data1[1], n_data2[1])
        else:
            check_answer_result = True

    check_answer_result = True
    os.system('cls')
    print(f"Sorry, that's wrong. Final score: {score}")


game()