unit = input("What is the temperature, Celcius (C) or Fahrenheit (F)?: ").upper()
temperature = float(input("Enter the temperature: "))

if unit == "C":
    temperature = round((temperature * (9/5)) + 32, 1)
    print(f"The temperature in Fahrenheit is: {temperature}°F")
elif unit == "F":
    temperature = round((temperature - 32) * (5/9), 1)
    print(f"The temperature in Celcius is: {temperature}°C")
else:
    print(f"The {unit} temperature is not a valid input")