menu = {"pizza": 249.99,
        "popcorn": 100,
        "burger": 50.25,
        "soda": 25.50,
        "nachos": 119.99,
        "lemonade": 40,
        "pretzel": 50,
        "chips": 35}
cart = []
total = 0

print("------- MENU -------")
for key, value in menu.items():
    print(f"{key:10}: \u20B1{value:.2f}")
print("--------------------")

while True:
        food = input("select an item (q to quit): ").lower()
        if food == "q":
                break
        elif menu.get(food) is not None:
                cart.append(food)
print("----- YOUR ORDER -----")
for food in cart:
        total += menu.get(food)
        print(food, end=" ")
print()
print(f"total is: {total:.2f}")
print("--------------------")