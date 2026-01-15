import math

print("Python Calculator")
print("1. Addition +")
print("2. Subtraction -")
print("3. Multuplication *")
print("4. Division /")
operatorChoice = input("Choose an operation (1-4): ")

if operatorChoice == "1":
    additionNumber1 = float(input("Enter your first number: "))
    additionNumber2 = float(input("Enter your second number: "))
    sum = additionNumber1 + additionNumber2
    print("")
    print(f"The sum is: {round(sum, 4)}")
elif operatorChoice == "2":
    subtractionNumber1 = float(input("Enter your first number: "))
    subtractionNumber2 = float(input("Enter your second number: "))
    difference = subtractionNumber1 - subtractionNumber2
    print(f"The difference is: {round(difference, 4)}")
elif operatorChoice == "3":
    multiplicationNumber1 = float(input("Enter your first number: "))
    multiplicationNumber2 = float(input("Enter your second number: "))
    product = multiplicationNumber1 * multiplicationNumber2
    print(f"The product is: {round(product, 4)}")
elif operatorChoice == "4":
    divisionNumber1 = float(input("Enter your numerator number: "))
    divisionNumber2 = float(input("Enter your denominator number: "))
    quotient = divisionNumber1 / divisionNumber2
    print(f"The quotient is: {round(quotient, 4)}")
else:
    print("Invalid operation")