# Formula
#BMI = weight(kg)
  #   -----------
  #  height ** 2(m**2)

height = input('Enter your height in m: ')
weight = input('Enter you weight in kg: ')

bmi_result = int(weight) / float(height)**2
print(f'Your BMI result is {int(bmi_result)}')

if bmi_result < 18.5:
    print('You are underweight')

elif bmi_result > 18.5 and bmi_result < 25:
    print('You are normal weight')
    
elif bmi_result > 25 and bmi_result < 30:
    print('You are overweight')

elif bmi_result > 30 and bmi_result <35:
    print('You are obese')

else:
    print('You are clinically obese')
