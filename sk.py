# menu of restaurant
menu = {
    'pizza': 60,
    'pasta': 40,
    'burger': 60,
    'salad': 70,
    'coffee': 80,
}

print("Welcome to Love Bite Restaurant")
print("pizza: 60 Rs\nPasta: 40 Rs\nBurger: 60 Rs\nsalad: 70 Rs\ncoffee: 80 Rs")

order_total = 0
order_item=[]

while True:
    item = input("Enter the item you want to order: ").lower()
    if item in menu:
        order_total += menu[item]
        order_item.append((item,menu[item]))
        print(f"Your item {item} has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu")

    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() != 'yes':
        break
print('\n')
print("YOUR BILL\n")
for  name,price in order_item:
    print(f".{name.capitalize()}: {price} RS")

print(f"The total amount to pay is {order_total} Rs")


