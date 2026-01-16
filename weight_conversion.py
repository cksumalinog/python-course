weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"You weight is: {round(weight , 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"You weight is: {round(weight , 2)} {unit}")
else:
    print(f"Unit {unit} is not a valid")