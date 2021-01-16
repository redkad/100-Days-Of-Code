import art

run = True

while run:
    print(art.logo)
    
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    w = input('Enter your message: ').lower()
    s = int(input('How many times will like to shift? '))
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    quit = False
    s = s%26


    def caesar(word, shift, direction):


        end_text = ''
        new_shift = 0

        if direction == 'decode':
            shift *= -1
        

        for w in range(len(word)):
            if word[w] in alphabets:

                for i in range(len(alphabets)):

                # print(i,w)
                    new_shift = i+shift

                    if word[w] == alphabets[i]:
                        # print(i,w)
                        if new_shift < len(alphabets):
                            # print(w, (i+shift))
                            end_text += alphabets[new_shift]
                            # print(encrypted)
                            

                        elif new_shift > len(alphabets):
                            out_of_range = new_shift - len(alphabets)
                            end_text += alphabets[out_of_range]

            else:
                end_text += word[w]            
        

        print(f'The {direction}d text is {end_text}')

    caesar(w, s, choice)
    again = input(f"Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()

    if again == 'no':
        print('Goodbye')
        run = False