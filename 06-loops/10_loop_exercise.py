menu = """
==============================
|| Shopping Cart            || 
|| Options:`                ||
||     1. Add product       ||
||     2. Delete product    ||
||     3. Show product list ||
||     4. Search product    ||
||     5. Count items       ||
||     6. Empty cart        ||
||     7. Exit              ||
==============================
"""

shopping_cart = ["Laptop", "Smartphone", "Headphones", "Mouse Gamer"]

option = ""

while option != "7":
    print(menu)

    option = input("Select an option (1-7): ")

    result = ""

    match option:
        case "1":
            new_product = input("Type the product to add name: ")
            if new_product not in shopping_cart:
                shopping_cart.append(new_product.strip())
                result = f"Shopping cart successfully updated: {shopping_cart}"
            else:
                result = f"{new_product} is already in the cart"
        case "2":
            delete_product = input("Type the product to delete name: ")
            if delete_product in shopping_cart:
                shopping_cart.remove(delete_product)
                result = f"Shopping cart successfully updated: {shopping_cart}"
            else:
                result = f"{delete_product} is not in the cart"
        case "3":
            if len(shopping_cart) < 1:
                result = "Your cart is empty"
            else:
                result = f"Your shopping cart: {shopping_cart.sort()}"
        case "4":
            search_product = input("Type the product to search name: ")
            product_exists = search_product in shopping_cart
            result = (
                "The product is in the cart" if product_exists else "Product not found"
            )
        case "5":
            count = len(shopping_cart)
            result = f"There are {count} your in the cart"
        case "6":
            shopping_cart.clear()
            result = "Shopping cart successfully cleared"
        case "7":
            result = "Program exited"
        case _:
            result = "Invalid option"

    print(result)
