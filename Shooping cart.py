# Creating the Shopping Cart
shopping_cart = []

# Function to Add a New Item into the Cart
def add_Item():
    # Reading the Item's information
    item = input("Enter Item Name: ")
    price = float(input("Enter Item Price: "))
    qty = int(input("Enter the Quantity: "))
    # Adding the Item into the Cart
    shopping_cart.append({'Item': item, 'Price': price, 'Quantity':qty})
    # Printing a message after adding the item
    print(f"{item} added to the cart successfully.")
    print()

def del_Item():
    view_Cart()
    d = int(input("Enter the Index to be deleted: "))
    shopping_cart.pop(d-1)
    print("After deletion - ")
    view_Cart()

def update_Item():
    view_Cart()
    i = int(input("Enter the Item Number you want to Modify: "))
    nq = int(input("Enter the New Quantity: "))
    shopping_cart[i-1] ['Quantity'] = nq
    print(F"{shopping_cart[i-1] ['Item']}'s Quanty chaned to {nq} successfully")
    print()
    view_Cart()
   
def view_Cart():
    if len(shopping_cart) == 0:
        print("Cart is Empty.")
    else:
        print("Items present in the Cart are:")
        print(F"Name \t Price \t Quantity")
        for index, item in enumerate(shopping_cart):
            print(f"{index + 1}. {item['Item']}\t ${item['Price']}\t{item['Quantity']}")
        print()

def calculate_Total():
    sum = 0
    print("Items present in the Cart are:")
    print(F"Name \t Price \t Quantity\t Total")
    for index, item in enumerate(shopping_cart):
        temp = item['Price'] * item['Quantity']
        sum = sum + temp
        print(f"{index + 1}. {item['Item']}\t ${item['Price']}\t{item['Quantity']}\t{temp}")
    print()
    print(f"Total cost: ${sum:.2f}")
    print()

while True:
    print("Welcome to XYZ Online Website")
    print("Pls find the options below: ")
    print("1. Add Item to Cart")
    print("2. View Cart")
    print("3. Calculate Cart Total")
    print("4. Modify the Item")
    print("5. Delete the Item")
    print("6. Quit")
    opt = int(input("Pls enter your choice [1 to 6]: "))
    print()
   
    if opt == 1:
        add_Item()
    elif opt == 2:
        view_Cart()
    elif opt == 3:
        calculate_Total()
    elif opt == 4:
        update_Item()
    elif opt == 5:
        del_Item()
    elif opt == 6:
        print("Thanks for visiting. See you soon.... Bye!")
        break
    else:
        print("Invalid Option, Try again..")