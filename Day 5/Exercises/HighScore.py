scores = input('Enter student scores: ').split(', ')

high_score = 0

for score in scores:
    if high_score < int(score):
        high_score = int(score)

print(f'The highest score in the class is: {high_score}')