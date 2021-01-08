your_name = input('Enter your name: ').lower()
her_name = input('Enter his or her name: ').lower()
name = your_name + her_name

true = 0
love = 0
m = ('t','r','u', 'e')
n = ('l','o','v', 'e')
c = len(m)
d = len(n)
count = 0
# print(count)

while count < c:
    times = name.count(m[count])
    true += times
    times1 = name.count(n[count])
    love+=times1
    count += 1

# greater = max(love, true)
# less = min(love, true)
# print(greater)
# print(less)
love_score = str(true) + str(love)
print(love_score)

if int(love_score) < 10 or int(love_score) > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos')

elif int(love_score) > 40 and int(love_score) < 50:
    print(f'Your score is: {love_score} you are alright together')

else:
    print(f'Your score is {love_score}')
# t = name.count('t')
# r = name.count('r')
# u = name.count('u')
# e = name.count('e')

# l = name.count('l')
# o = name.count('o')
# v = nam

# count_true = t + r + u + e