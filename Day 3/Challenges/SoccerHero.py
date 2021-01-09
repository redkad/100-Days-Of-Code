print('''_____       .-"'""""''-.
     |__,-'"      _.,/  ;
     }         ,-'   |  ;
     |         ;    /" ,'
     {          '..;,./_       o
     |-.,_            ;";     "|\                       AsH/PjP
"""""     '-.,__.------'______/)_____________________________________
            /                '..' ()    /                           /
           /________   o               /    . \     o     _________/
        /|/o ____   / /|"             /    (|==;o        /  o___/|\\
       /_|/"'   /  /-, )\       _.--"/"-,   ' "     _.--/  ~|\ / |_\\
______/_//)   /  /   :'..'     /    /    :  "/-    /   /  / (\/_/__/____/""|
"""""/|"'..' /  /   /         (    /    /   /)    (   /  / '..|\\""/""""""""
    /_|     /  /.-'      o    `._ /_.-'           `. /  /     |_\/
     /-----'  /         /|"     /         / .       /  `-----/
    /--------'          /)     /       o;==|)    __`--------/
   /                   '..'   /          " '    '..'       /
  /__________________________/____________________________/''')
  
print("\nYou're in the final moment of the game and you've got the ball. Right in fron't of you is an opponent waiting to defend the ball. \nOn your left is your team mate waiting for you to pass him the ball. \nYou look down your right and saw a free space but there's an opponent at the far end.")
choice = input('What do you do.? Type "pass" to pass to your team mate on the left or Type "middle" to dribble your opponent in front of you or Type "right" to go down the free space on the right:\n\n').lower()    

if choice == 'pass':
    print('\nYou pass the ball to your teammate but unfortunately, your pass was intercepted.\nThe refree blow the final whitstle. Game Over!')

elif choice == 'middle':
    print('\nYou dribble and nutmeg your opponent. The fans applaud for your wonderful skills')
    choice = input('You are one on one with the goalkeeper. What do you do? Type "dribble" to dribble the goalkeeper. Type "left" to play a shot down the left and Type "right" to play a shot down the right.\n\n').lower()
    if choice == 'dribble':
        print('\nYou tried to dribble the goalkeeper but he ends up holding your leg. The refree has blown the whitstle. It\'s a penalty.')
        choice = input("It's a penalty in the final moments of the game. You step up to take the penalty. Where do you play the ball to? Type \"left\", \"middle\" or \"right\"").lower()
        if choice == 'right':
            print('\nYou play the ball with power down the right post but unfortunately, it hits the post and the goalkeeper catches the ball. The refree has blown the fianl whitstle. Game Over!')

        elif choice == 'left':
            print('You play the ball gently but with power down the left post. It\'s a gooooooooaaaaaaaaaaaallllll. The fans applaud you for your effort.\nthe refree has blown the final whitlse. You\'ve won the game Congratulations.')
        
        elif choice == 'middle':
            print('You play the ball beautifully down the middle but the goalkeeper catches it. The refree has blown the fianl whitstle. Game Over!')
        

    elif choice == 'right':
        print('\nYou play the ball down the right post but the goalkeeper punches the ball. The refree has blown the fianl whitstle. Game Over!')

    elif choice == 'left':
        print('\nYou play the ball down the left post but that is your weaker foot. You missed. Game Over!.')

elif choice == 'right':
    print('\nYou tap the ball with speed pass your opponent in front of you and ended up loosing the ball.\nThe refree blow the final whitstle. Game Over!')

else:
    print('\nWrong input')

