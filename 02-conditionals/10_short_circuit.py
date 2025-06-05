# Short circuit

# OR
True or print("Hello World")
False or print("Hello World")

# AND
True and print("Hello World")
False and print("Hello World")

# Real use case: to avoid error by possible nullish values
name = None
# name = "Pepe"

name and print(name.upper())
