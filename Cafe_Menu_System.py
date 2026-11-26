import datetime  # To get the current date and time

# Menu categories with items and their prices
menu = {
    "FAST FOOD": {
        "PIZZA": 520,
        "BURGER": 410,
        "FRIES": 100,
    },
    "RICE": {
        "CHICKEN PALAO": 540,
        "PALAO KABAB": 400,
        "PALAO": 270,
    },
    "DRINKS": {
        "COLD DRINK": 100,
        "JUICE": 60,
    },
}

# Alternative names for items to make user input flexible.
# "RICE" is not an alias because it is a category name: typing it shows the rice items.
aliases = {
    "PIZZA": ["PIZZA", "PIZA"],
    "BURGER": ["BURGER", "BARGER", "BAGRAR"],
    "FRIES": ["FRIES", "CHIPS"],
    "CHICKEN PALAO": ["CHICKEN PALAO", "PALAO CHICKEN", "CHICKENPALAO"],
    "PALAO KABAB": ["PALAO KABAB", "KABAB PALAO", "PALAOKABAB"],
    "PALAO": ["PALAO", "CHAWAL"],
    "COLD DRINK": ["COLD", "SOFTDRINK", "COLD DRINK", "COLA", "COKE", "PEPSI", "COLDDRINK"],
    "JUICE": ["JUICE", "ORANGE", "APPLE"],
}

# Convert all menu items into a single dictionary for easy price lookup
flat_menu = {}
for category_items in menu.values():
    flat_menu.update(category_items)


def print_category(category):
    # Show the items and prices of one category
    print(f"Available items in {category}:")
    for item, price in menu[category].items():
        print(f"  {item:<15} : Rs {price}")


def print_menu():
    # Show every category with its items
    print("------ MENU CATEGORIES ------")
    for category, items in menu.items():
        print(f"\n[{category}]")
        for item, price in items.items():
            print(f"  {item:<15} : Rs {price}")
    print("\n-----------------------------")


def find_category(text):
    # A category matches when the typed text is its exact name or starts it (at least 3 letters)
    for category in menu:
        if text == category or (len(text) >= 3 and category.startswith(text)):
            return category
    return None


def find_item(text):
    # Match the typed name with the aliases of every menu item
    for real_item, keywords in aliases.items():
        if text in keywords:
            return real_item
    return None


def parse_order_part(part):
    # "PIZZA 2" -> ("PIZZA", 2); "PIZZA" -> ("PIZZA", 1)
    words = part.split()
    if words and words[-1].isdigit():
        return " ".join(words[:-1]), int(words[-1])
    return " ".join(words), 1


def print_receipt(customer_name, order_time, order_summary, order_total):
    print("\n========== ORDER RECEIPT ==========")
    print(f"Customer Name : {customer_name}")
    print(f"Order Time    : {order_time}")
    print("\nItems Ordered:")
    print("-------------------------------")
    for item, details in order_summary.items():
        print(f"{item:<15}  Quantity: {details['qty']}  "
              f"Price: Rs {details['price']}  Total: Rs {details['subtotal']}")
    print("-------------------------------")
    print(f"TOTAL BILL    : Rs {order_total}")
    print("Thank you for visiting our cafe!")
    print("==================================\n")


def main():
    # Greeting
    print("\n****************************************")
    print("  ASSALAMUALAIKUM! WELCOME TO OUR CAFE  ")
    print("****************************************\n")
    print("What would you like to eat?\n")
    print_menu()

    customer_name = input("\nPlease enter your name: ").strip().title()
    order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    order_total = 0
    order_summary = {}

    # Keep taking orders until the user types "exit" or "end"
    while True:
        print("\nEnter your order (e.g., pizza 2, cold, burger)")
        print("Type a category name (fast food, rice, drinks) to see its items.")
        print("If you are done, type 'exit' or 'end'.\n")
        user_input = input("Your order: ").strip().upper()

        if user_input.lower() in ("exit", "end"):
            break
        if not user_input:
            continue

        # A single category name shows that category's items
        category = find_category(user_input)
        if category:
            print_category(category)
            continue

        # Several items can be ordered at once, separated by commas
        for part in user_input.split(","):
            part = part.strip()
            if not part:
                continue

            input_item, quantity = parse_order_part(part)
            matched_item = find_item(input_item)

            if not matched_item:
                print(f"[X] Sorry, '{input_item}' is not available on our menu.")
                continue
            if quantity < 1:
                print(f"[X] Quantity for {matched_item} must be at least 1.")
                continue

            price = flat_menu[matched_item]
            subtotal = price * quantity
            order_total += subtotal

            # Update the item if it was ordered before, otherwise add it
            if matched_item in order_summary:
                order_summary[matched_item]["qty"] += quantity
                order_summary[matched_item]["subtotal"] += subtotal
            else:
                order_summary[matched_item] = {
                    "qty": quantity,
                    "price": price,
                    "subtotal": subtotal,
                }
            print(f"[OK] {quantity} {matched_item} added. Subtotal: Rs {subtotal}")

    # Print the receipt after the order is complete
    if order_summary:
        print_receipt(customer_name, order_time, order_summary, order_total)
    else:
        print("\nNo items were ordered. Thank you!")


if __name__ == "__main__":
    main()
