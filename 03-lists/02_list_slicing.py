shopping_cart = ["T-Shirt", "Pants", "Shoes", "Glasses"]

print(shopping_cart[0])

# Slicing a list. Similar to the string slice because strings behaves like a list
# ! List slicing DO NOT mutate de list, creates a new memory reference
sliced_list = shopping_cart[0:2]

print(sliced_list)

# Accesing a list list value with indexes and assign a new value, mutate the actual list
# Opposite to the string that are inmutable

shopping_cart[1] = "Hoody"

print(shopping_cart)
