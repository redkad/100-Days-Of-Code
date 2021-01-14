import random
import hangman, hangmanWords

print(hangman.logo)
blanks = []

lives = 0

chosen_word = random.choice(hangmanWords.word_list)

for _ in range(len(chosen_word)):
        blanks.append('_')

while '_' in blanks and lives < 7:

    entered = input('\nEnter a letter: ').lower()

    if entered in blanks :
        print(f'You have already guessed the letter {entered}')

    count = 0

    for char in chosen_word:
        if entered == char:
            blanks[count] = entered

        count+=1


    

    if entered not in chosen_word:
        print(' '.join(blanks))
        print(f'Wrong guess. You have {6 - lives} tries left\n')
        print(hangman.HANGMANPICS[lives])
        lives += 1
    else:    
        print(' '.join(blanks))   

    
if '_' not in blanks:

    print("You've Won")

else:
    print(f"You've lost. The word was {chosen_word}")