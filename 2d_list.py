groceries = [["apple", "orange", "banana"],
             ["potato", "cabbage", "kangkong"],
             ["pork", "chicken", "beef"]]

for grocery in groceries:
    for collection in grocery:
        print(collection, end=" ")
    print()