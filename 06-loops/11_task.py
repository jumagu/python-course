inventory = {
    "chocolate": 10,
    "gummies": 5,
    "palette": 8,
    "gum": 2,
    "alfajor": 8,
    "cookies": 12,
}

message = """
Welcome to the groseries shop, DevCandy!

What do you want to take?

Inventory:
"""

print(message)

for item, price in inventory.items():
    print(f"{item.capitalize()} - ${price:.2f}")

text = """
Type the item you want (Press Enter to confirm)
Otherwise, type 'exit' if you are done with your order.
>> """

cart = []

while True:
    choise = input(text)

    if choise == "exit":
        break

    choise = choise.lower().strip()

    if choise in inventory:
        cart.append(choise)
        print(f"\nYou added {choise} to your cart.")
    else:
        print(f"\n{choise} is not in the inventory!")

if len(cart) == 0:
    print("\nCome back soon!\n")
else:
    total = 0
    print("\nYour cart:")
    for item in cart:
        print(f"{item.capitalize()} - ${inventory[item]:.2f}")
        total += inventory[item]
    print(f"\nTotal due: ${total:.2f}\n")
