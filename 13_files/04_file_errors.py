try:
    with open("another_file.py", mode="r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exits.")
except PermissionError:
    print("You do not have permission to read this file.")
except Exception as e:
    print(f"An error occured while reading the file: {e}")
