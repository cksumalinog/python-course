age = int(input("Enter your age: "))
if age >= 150:
    print("You are ancient")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't born yet")
else:
    print("You must be 18+ to sign up")

response = input("Would you like to be punched? (Y/N): ")
if response == "Y" :
    print("/*Punched you in the face")
else:
    print("Nahhh...")

name = input("Enter your name yah: ")
if name == "":
    print("sino ka?")
else:
    print(f"Kumusta ka pareng {name}")