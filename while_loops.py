name = input("What is your name?: ")
while name == "":
    print("You didn't entered a name.")
    name = input("Enter your name: ")
print(f"Hello, {name}")
print()
age = int(input("How old are you?:  "))
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old.")
print()
food = input('What is your favourite food? (Type "q" to Quit): ')
while not food == "q":
    print(f"You like {food}")
    food = input('What is your other favourite food? (Press "q" to Quit): ')
print()
num = int(input("Enter a # between 1-10: "))
while num < 1 or num > 10:
    print(f"Number {num} does not exist in the range of numbers")
    num = int(input("Enter a # between 1-10: "))
print(f"You number is {num}")
grade = float(input("Enter your Grades: "))
while grade < 75:
    print("Enter a valid grade")
    grade = float(input("Enter your Grades: "))
print(f"Your grade {grade} is valid, you can now enroll.")