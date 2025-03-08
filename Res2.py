
#RESTAURANT MANAGEMENT PROJECT
# FIRST TIME PROJECT RUNNING ON DUAL CORE AND 4GIG RAM
mn = [
    {"itm": "Burger", "prc": 5.0, "stk": 20},
    {"itm": "Pizza", "prc": 8.0, "stk": 10},
    {"itm": "Pasta", "prc": 7.0, "stk": 15},
    {"itm": "Salad", "prc": 4.0, "stk": 25}
]

while True:
    print("\n--- Restaurant Management ---")
    print("1. View Menu")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Take Order")
    print("6. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        print("\n--- Menu ---")
        for itm in mn:
            print(itm['itm'] + ": $" + str(itm['prc']) + " (Stock: " + str(itm['stk']) + ")")

    elif ch == '2':
        nm = input("Enter new item name: ").capitalize()
        prc = float(input("Enter price for " + nm + ": "))
        stk = int(input("Enter stock for " + nm + ": "))
        mn.append({"itm": nm, "prc": prc, "stk": stk})
        print(nm + " added to menu.")

    elif ch == '3':
        nm = input("Enter item name to update: ").capitalize()
        for itm in mn:
            if itm['itm'] == nm:
                itm['prc'] = float(input("Enter new price for " + nm + " (current: $" + str(itm['prc']) + "): "))
                itm['stk'] = int(input("Enter new stock for " + nm + " (current: " + str(itm['stk']) + "): "))
                print(nm + " updated.")
                break
        else:
            print("Item not found.")

    elif ch == '4':
        nm = input("Enter item name to remove: ").capitalize()
        for itm in mn:
            if itm['itm'] == nm:
                mn.remove(itm)
                print(nm + " removed from menu.")
                break
        else:
            print("Item not found.")

    elif ch == '5':
        ord = {}
        print("\n--- Place Order ---")
        while True:
            nm = input("Enter item name to order (or 'done' to finish): ").capitalize()
            if nm == 'Done':
                break
            for itm in mn:
                if itm['itm'] == nm:
                    qty = int(input("Enter quantity (available: " + str(itm['stk']) + "): "))
                    if qty <= itm['stk']:
                        if nm in ord:
                            ord[nm] += qty
                        else:
                            ord[nm] = qty
                        itm['stk'] -= qty
                        print("Added " + str(qty) + " " + nm + "(s) to order.")
                    else:
                        print("Not enough stock.")
                    break
            else:
                print("Item not available.")
        print("\n--- Order Summary ---")
        ttl = 0
        for nm, qty in ord.items():
            prc = next(itm['prc'] for itm in mn if itm['itm'] == nm)
            cst = prc * qty
            ttl += cst
            print(nm + ": " + str(qty) + " x $" + str(prc) + " = $" + format(cst, ".2f"))
        print("Total: $" + format(ttl, ".2f"))

    elif ch == '6':
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
