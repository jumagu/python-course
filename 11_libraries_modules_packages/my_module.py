def greet():
    print("Hello from my module")


# This only be executed if the file is directly executed.
# E.g. >> pyhton my_module.py
if __name__ == "__main__":
    print("This module is being executed directly!")
    greet()

print("This is the main file.")
