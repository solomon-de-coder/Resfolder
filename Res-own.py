menu = [
    {"item": "Burger", "price": 5.0, "stock": 20},
    {"item": "Pizza", "price": 8.0, "stock": 10},
    {"item": "Pasta", "price": 7.0, "stock": 15},
    {"item": "Salad", "price": 4.0, "stock": 25}
]

def view_menu():
    print("\n--- Menu ---")
    for item in menu:
        print(item['item'] + ": $" + str(item['price']) + " (Stock: " + str(item['stock']) + ")")

def add_item():
    name = input("Enter new item name: ").capitalize()
    price = float(input("Enter price for " + name + ": "))
    stock = int(input("Enter stock for " + name + ": "))
    menu.append({"item": name, "price": price, "stock": stock})
    print(name + " added to menu.")

def update_item():
    name = input("Enter item name to update: ").capitalize()
    for item in menu:
        if item['item'] == name:
            item['price'] = float(input("Enter new price for " + name + " (current: $" + str(item['price']) + "): "))
            item['stock'] = int(input("Enter new stock for " + name + " (current: " + str(item['stock']) + "): "))
            print(name + " updated.")
            return
    print("Item not found.")

def remove_item():
    name = input("Enter item name to remove: ").capitalize()
    for item in menu:
        if item['item'] == name:
            menu.remove(item)
            print(name + " removed from menu.")
            return
    print("Item not found.")

def take_order():
    order = {}
    print("\n--- Place Order ---")
    while True:
        name = input("Enter item name to order (or 'done' to finish): ").capitalize()
        if name == 'Done':
            break
        for item in menu:
            if item['item'] == name:
                qty = int(input("Enter quantity (available: " + str(item['stock']) + "): "))
                if qty <= item['stock']:
                    if name in order:
                        order[name] += qty
                    else:
                        order[name] = qty
                    item['stock'] -= qty
                    print("Added " + str(qty) + " " + name + "(s) to order.")
                else:
                    print("Not enough stock.")
                break
        else:
            print("Item not available.")
    print("\n--- Order Summary ---")
    total = 0
    for name, qty in order.items():
        price = next(item['price'] for item in menu if item['item'] == name)
        cost = price * qty
        total += cost
        print(name + ": " + str(qty) + " x $" + str(price) + " = $" + format(cost, ".2f"))
    print("Total: $" + format(total, ".2f"))

def main_menu():
    print("\n--- Restaurant Management ---")
    print("1. View Menu")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Take Order")
    print("6. Exit")

while True:
    main_menu()
    choice = input("Enter choice: ")
    if choice == '1':
        view_menu()
    elif choice == '2':
        add_item()
    elif choice == '3':
        update_item()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        take_order()
    elif choice == '6':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
