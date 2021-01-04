# Formula
#BMI = weight(kg)
  #   -----------
  #  height ** 2(m**2)

height = input('Enter your height in m: ')
weight = input('Enter you weight in kg: ')

bmi_result = int(weight) / float(height)**2
print(f'Your BMI result is {int(bmi_result)}')