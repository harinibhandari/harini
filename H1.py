#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# Load inventory data
inventory = pd.read_csv('inventory.csv')
# Define functions for user options
def view_inventory():
    print(inventory[['Item Number', 'Item Name', 'Quantity', 'Price']])
def update_items():
    global inventory
    item_number = int(input("Enter item number: "))
    if item_number in inventory['Item Number'].values:
        new_quantity = int(input("Enter new quantity: "))
        new_price = float(input("Enter new price: "))
        inventory.loc[inventory['Item Number'] == item_number, 'Quantity'] = new_quantity
        inventory.loc[inventory['Item Number'] == item_number, 'Price'] = new_price
    else:
        item_name = input("Enter item name: ")
        new_item = pd.DataFrame({'Item Number': [item_number], 'Item Name': [item_name], 'Quantity': [int(input("Enter quantity: "))], 'Price': [float(input("Enter price: "))]})
        inventory = pd.concat([inventory, new_item], ignore_index=True)
    inventory.to_csv('inventory.csv', index=False)
def modify_quantity():
    item_number = int(input("Enter item number: "))
    if item_number in inventory['Item Number'].values:
        new_quantity = int(input("Enter new quantity: "))
        inventory.loc[inventory['Item Number'] == item_number, 'Quantity'] = new_quantity
        print("Quantity updated successfully.")
    else:
        print("Item not found in inventory.")
# Define functions for customer options
def view_inventory_customer():
    print(inventory[['Item Number', 'Item Name', 'Quantity', 'Price']])
def add_to_cart():
    item_number = int(input("Enter item number: "))
    if item_number in inventory['Item Number'].values:
        quantity = int(input("Enter quantity: "))
        if inventory.loc[inventory['Item Number'] == item_number, 'Quantity'].values[0] < quantity:
            print("Not enough stock available.")
        else:
            item_name = inventory.loc[inventory['Item Number'] == item_number, 'Item Name'].values[0]
            item_price = inventory.loc[inventory['Item Number'] == item_number, 'Price'].values[0]
            cart_item = pd.DataFrame({'Item Number': [item_number], 'Item Name': [item_name], 'Quantity': [quantity], 'Price': [item_price]})
            if 'Cart' not in globals():
                global Cart
                Cart = cart_item
            else:
                Cart = pd.concat([Cart, cart_item], ignore_index=True)
            inventory.loc[inventory['Item Number'] == item_number, 'Quantity'] -= quantity
            print("Item added to cart.")
    else:
        print("Item not found in inventory.")
def bill():
    if 'Cart' not in globals():
        print("Cart is empty.")
    else:
        total_price = 0
        print("Item Number\tItem Name\tPrice\tQuantity")
        for i, row in Cart.iterrows():
            item_number = row['Item Number']
            item_name = row['Item Name']
            item_price = row['Price']
            quantity = row['Quantity']
            total_price += item_price * quantity
            print(f"{item_number}\t\t{item_name}\t\t{item_price}\t{quantity}")
        print(f"\nTotal Price: {total_price}\nSupermarket Name: XYZ")
def payment_options():
    print("Payment options:\n1. Cash\n2. Credit Card\n3. Debit Card")
# Main program loop
while True:
    print("\nWelcome to Supermarket\n1. User\n2. Customer\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        while True:
            print("\nUser Options\n1. View Inventory\n2. Update Items\n3. Modify Quantity\n4. Exit")
            user_choice = int(input("Enter your choice: "))
            if user_choice == 1:
                view_inventory()
            elif user_choice == 2:
                update_items()
            elif user_choice == 3:
                modify_quantity()
            elif user_choice == 4:
                break
    elif choice == 2:
        while True:
            print("\nCustomer Options\n1. View Inventory\n2. Add to Cart\n3. Bill\n4. Payment Options\n5. Exit")
            customer_choice = int(input("Enter your choice: "))
            if customer_choice == 1:
                view_inventory_customer()
            elif customer_choice == 2:
                add_to_cart()
            elif customer_choice == 3:
                bill()
            elif customer_choice == 4:
                payment_options()
            elif customer_choice == 5:
                break
            else:
                print("Invalid choice. Please enter a valid option.")
    elif choice == 3:
        print("Visit Again. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


# In[ ]:




