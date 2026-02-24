import time
daily_sales = []

while True:
    print("--- Daily Sales Tracker ---\n"
          "1. Enter a new sale\n"
          "2. View all the sales\n"
          "3. Calculate total revenue\n"
          "4. Exit\n"
          "--------------------------")
    option_answer = input("Choose an option (1-4): ")

    if option_answer == "1":
        isSales = True
        print("Type q to quit")
        while isSales:
            sales_input = input("\nEnter Sales: ")
            if sales_input.lower().strip() == "q" or sales_input.lower().strip() == "quit":
                isSales = False
            else:
                sales = float(sales_input)
                daily_sales.append(sales)
                print(f"Added {sales} to today's sale")
    elif option_answer == "2":
        print("\n--- Daily Sales ---")
        for sale_count, daily_sale in enumerate(daily_sales, start=1):
            print(f"Sales #{sale_count}: {daily_sale}")
        print("---------------------------\n")
    elif option_answer == "3":
        print("\n--- Total Revenue ---")
        total = 0
        for revenue in daily_sales:
            total += revenue
        print(f"Total: {total}")
        print("-----------------------\n")
    elif option_answer == "4":
        print("Shutting Down....")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("System Shutdown.")
        break