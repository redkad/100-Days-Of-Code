print('Welcome to Treasure Map\n')

r1 = ['🥳', '🥳', '🥳']
r2 = ['🥳', '🥳', '🥳']
r3 = ['🥳', '🥳', '🥳']

map = [r1, r2, r3]
print(f'{r1}\n{r2}\n{r3}\n')

position = input('Where do you want to put the treasure? ')
col = int(position[0])
row = int(position[1])
plot = map[row - 1][col - 1] = 'X '
print(f'\n{r1}\n{r2}\n{r3}')