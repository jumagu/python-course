numbers = [1, 2, 3, 4, 5]
vocals = ["a", "e", "i", "o", "u"]

mix = [2, True, "Hola", [1, 2, 3], 10.5]

shopping_cart = ["Laptop", "Smartphone", "Headphones"]

print(shopping_cart)

# Copying a list
# ! remember that objects in python keep its reference until they get removed by the garbage collector for not being used

# ? Keeps the same reference
# new_cart = shopping_cart

# Shallow copy
# new_cart = shopping_cart.copy()

# More cleaner way to create a shallow copy
new_cart = shopping_cart[:]
