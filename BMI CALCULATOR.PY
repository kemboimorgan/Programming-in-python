# BMI CALCULATOR


weight = int(input("Enter your weight in kilograms: "))
height = int(input("Enter your height in meters: "))

bmi = weight / (height ** 2)


print(f"Your BMI is: bmi:.2f")

if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Category: Normal weight")
elif 25 <= bmi <= 29.9:
    print("Category: Overweight")
else:  # bmi >= 30
    print("Category: Obesity")

