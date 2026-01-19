price1 = 3.14159
price2 = -987.65
price3 = 321.32

# Decimals
print(f"Price 1 is ₱{price1:.3f}")
print(f"Price 2 is ₱{price2:.3f}")
print(f"Price 3 is ₱{price3:.3f}")
print("")
#Concatenation / space
print(f"Price 1 is ₱{price1:10}")
print(f"Price 2 is ₱{price2:10}")
print(f"Price 3 is ₱{price3:10}")
print("")
#Preceeding 0s
print(f"Price 1 is ₱{price1:010}")
print(f"Price 2 is ₱{price2:010}")
print(f"Price 3 is ₱{price3:010}")
print("")
#Left Justified
print(f"Price 1 is ₱{price1:<10}")
print(f"Price 2 is ₱{price2:<10}")
print(f"Price 3 is ₱{price3:<10}")
print("")
#Right Justified
print(f"Price 1 is ₱{price1:>10}")
print(f"Price 2 is ₱{price2:>10}")
print(f"Price 3 is ₱{price3:>10}")
print("")
#Center Line
print(f"Price 1 is ₱{price1:^10}")
print(f"Price 2 is ₱{price2:^10}")
print(f"Price 3 is ₱{price3:^10}")
print("")
#Precedes
print(f"Price 1 is ₱{price1:+}")
print(f"Price 2 is ₱{price2:-}")
print("")
#Thousands seperator
price1 = 1223.14159
price2 = -1987.65
price3 = 3432421.32
print(f"Price 1 is ₱{price1:+,.2f}")
print(f"Price 2 is ₱{price2:+,.2f}")
print(f"Price 3 is ₱{price3:+,.2f}")