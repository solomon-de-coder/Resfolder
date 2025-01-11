def main_menu():
    print("\n--- Restaurant Management System ---")
    print("1. View Menu")
    print("2. Add Item to Menu")
    print("3. Update Item in Menu")
    print("4. Remove Item from Menu")
    print("5. Take Order")
    print("6. View Inventory")
    print("7. Exit")

# Initialize menu and inventory
default_menu = {
    "Burger": {"price": 5.0, "stock": 20},
    "Pizza": {"price": 8.0, "stock": 10},
    "Pasta": {"price": 7.0, "stock": 15},
    "Salad": {"price": 4.0, "stock": 25}
}

menu = default_menu.copy()

def view_menu():
    print("\n--- Menu ---")
    for item, details in menu.items():
        print(f"{item}: ${details['price']} (Stock: {details['stock']})")

def add_item():
    item_name = input("Enter the name of the item to add: ").capitalize()
    if item_name in menu:
        print("Item already exists. Use 'Update Item' to modify it.")
        return
    price_input = input(f"Enter the price for {item_name}: ")
    stock_input = input(f"Enter the stock for {item_name}: ")
    if price_input.replace('.', '', 1).isdigit() and stock_input.isdigit():
        price = float(price_input)
        stock = int(stock_input)
        menu[item_name] = {"price": price, "stock": stock}
        print(f"{item_name} added to the menu.")
    else:
        print("Invalid input. Please enter numeric values for price and stock.")

def update_item():
    item_name = input("Enter the name of the item to update: ").capitalize()
    if item_name not in menu:
        print("Item not found in the menu.")
        return
    price_input = input(f"Enter the new price for {item_name} (current: ${menu[item_name]['price']}): ")
    stock_input = input(f"Enter the new stock for {item_name} (current: {menu[item_name]['stock']}): ")
    if price_input.replace('.', '', 1).isdigit() and stock_input.isdigit():
        price = float(price_input)
        stock = int(stock_input)
        menu[item_name] = {"price": price, "stock": stock}
        print(f"{item_name} updated.")
    else:
        print("Invalid input. Please enter numeric values for price and stock.")

def remove_item():
    item_name = input("Enter the name of the item to remove: ").capitalize()
    if item_name in menu:
        del menu[item_name]
        print(f"{item_name} removed from the menu.")
    else:
        print("Item not found in the menu.")

def take_order():
    order = {}
    print("\n--- Place Order ---")
    while True:
        item_name = input("Enter the item name to order (or type 'done' to finish): ").capitalize()
        if item_name.lower() == 'done':
            break
        if item_name not in menu:
            print("Item not found in the menu. Please try again.")
            continue
        quantity_input = input(f"Enter quantity for {item_name} (available: {menu[item_name]['stock']}): ")
        if quantity_input.isdigit():
            quantity = int(quantity_input)
            if quantity > menu[item_name]['stock']:
                print("Insufficient stock. Please try again.")
                continue
            if item_name in order:
                order[item_name] += quantity
            else:
                order[item_name] = quantity
            print(f"{quantity} {item_name}(s) added to the order.")
        else:
            print("Invalid input. Please enter a numeric value for quantity.")

    print("\n--- Order Summary ---")
    total_cost = 0
    for item, qty in order.items():
        cost = qty * menu[item]['price']
        total_cost += cost
        menu[item]['stock'] -= qty
        print(f"{item}: {qty} x ${menu[item]['price']} = ${cost:.2f}")
    print(f"Total Bill: ${total_cost:.2f}")

def view_inventory():
    print("\n--- Inventory ---")
    for item, details in menu.items():
        print(f"{item}: Stock: {details['stock']}")

# Main execution loop
while True:
    main_menu()
    choice = input("\nEnter your choice: ")

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
        view_inventory()
    elif choice == '7':
        print("Exiting the Restaurant Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
