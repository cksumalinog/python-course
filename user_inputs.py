# input() = A function that prompts the user to enter data
#           Return the entered data as a string

#Shopping Cart Program
item = input("what would you like to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many will you buy?:"))
total = quantity * price
print("")
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: {total}")

# Rectangle Area Calculator
length = float(input("Enter Length:"))
width = float(input("Enter width:"))
area = length * width
print(f"The rectangle's area is: {area}cm²")

# Some stuffs
name = input("What is your name?:")
print(f"Hello there, {name}!")
age = int(input(f"And how old are you, {name}?:"))
if 12 < age < 40:
    print(f"ohh, you're a teenager")
if  0 < age < 13:
    print("still young kiddo")
if 40 < age:
    print("too old...")