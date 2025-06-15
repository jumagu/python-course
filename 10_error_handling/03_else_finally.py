def divide_numbers():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ValueError:
        print("Please enter valid numbers only.")
    except ZeroDivisionError:
        print("Can't divide between zero.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    # If no exception
    else:
        return result
    # Finally: alaways executed either an error is caugth or not.
    finally:
        print("Thanks for using our calculator!")


result = divide_numbers()

if result:
    print(f"Result: {result}")
