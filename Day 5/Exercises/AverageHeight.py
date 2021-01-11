heights = input('Enter student heights: ').split(', ')

student_heights = 0
count = 0

for height in heights:
    student_heights += int(height)
    count += 1

new_height = (student_heights / count)
print(round(new_height))