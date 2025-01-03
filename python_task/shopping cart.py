items = ['Bread', 'Cookies', 'Butter', 'Cheese', 'Yoghurt']
prices = [40, 80, 120, 180, 60]
cart = []

def add_item(cart):
    item = input("Enter the item name to add: ")
    if item in items:
        quantity = int(input("Enter the quantity: "))
        cart.append((item, quantity))
        print(f"{item} added to the cart.")
    else:
        print("Item not available.")

def remove_item(cart):
    item = input("Enter the item name to remove: ")
    for i, (cart_item, quantity) in enumerate(cart):
        if cart_item == item:
            del cart[i]
            print(f"{item} removed from the cart.")
            return
    print("Item not in the cart.")

def view_cart(cart):
    if cart:
        print("\nItems in the cart:")
        for item, quantity in cart:
            print(f"{item}: {quantity}")
    else:
        print("Cart is empty.")

def update_quantity(cart):
    item = input("Enter the item name to update: ")
    for i, (cart_item, quantity) in enumerate(cart):
        if cart_item == item:
            new_quantity = int(input("Enter the new quantity: "))
            cart[i] = (item, new_quantity)
            print(f"Quantity of {item} updated to {new_quantity}.")
            return
    print("Item not in the cart.")

def print_bill(cart):
    total = 0
    print("\nBill:")
    for item, quantity in cart:
        price = prices[items.index(item)]
        cost = price * quantity
        total += cost
        print(f"{item}: {quantity} x {price} = {cost}")
    print(f"Total: {total}")

# Example usage
while True:
    print("\n1. Add item")
    print("\n2. Remove item")
    print("\n3. View cart")
    print("\n4. Update quantity")
    print("\n5. Print bill")
    print("\n6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_item(cart)
    elif choice == 2:
        remove_item(cart)
    elif choice == 3:
        view_cart(cart)
    elif choice == 4:
        update_quantity(cart)
    elif choice == 5:
        print_bill(cart)
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")