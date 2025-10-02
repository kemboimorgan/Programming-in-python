# Program to check if a person is eligible to vote

citizen = input("Are you a Kenyan citizen? (yes/no): ").lower()
age = int(input("Enter your age: "))

if citizen == "yes" and age >= 18:
    print("You are eligible to vote.")
else:
    print("Sorry, you are not eligible to vote.")