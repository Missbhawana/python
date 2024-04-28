def add_item(inventory, item, quantity):

    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def remove_item(inventory, item, quantity):

    if item in inventory:
        if inventory[item] <= quantity:
            del inventory[item]
        else:
            inventory[item] -= quantity
    else:
        print("Item not found in inventory.")

def display_inventory(inventory):

    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_item_quantity(inventory, item, quantity):

    if item in inventory:
        inventory[item] = quantity
    else:
        print("Item not found in inventory.")

def inventory():
    inventory = {}
    while True:
        print("\n1. Add Item\n2. Remove Item\n3. Display Inventory\n4. Update Item Quantity\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            item = input("Enter the name of the item: ")
            quantity = int(input("Enter the quantity: "))
            add_item(inventory, item, quantity)
            print("Item added to inventory.")
        elif choice == '2':
            item = input("Enter the name of the item: ")
            quantity = int(input("Enter the quantity to remove: "))
            remove_item(inventory, item, quantity)
            print("Item removed from inventory.")
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            item = input("Enter the name of the item: ")
            quantity = int(input("Enter the new quantity: "))
            update_item_quantity(inventory, item, quantity)
            print("Item quantity updated.")
        elif choice == '5':
            print("Exiting inventory system.")
            break
        else:
            print("Invalid choice. Please try again.")

inventory()
