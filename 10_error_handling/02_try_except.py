def divide_numbers():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b

        return result
    except ValueError:
        print("Please enter valid numbers only.")
    except ZeroDivisionError:
        print("Can't divide between zero.")
    except Exception as e:
        print(f"Unexpected error: {e}")


result = divide_numbers()

if result:
    print(f"Result: {result}")
