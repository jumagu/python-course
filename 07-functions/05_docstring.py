# Documeting a function using DocString


def hello(greet="Hello", name="Guest"):
    """Info: Thuis function helps you to greet someone.

    Args:
        greet (str, optional): _description_. Defaults to "Hello".
        name (str, optional): _description_. Defaults to "Guest".
    """
    print(f"{greet}, {name}")


hello()


def multiply(a: int, b: int) -> int:
    """Multiplies two given numbers

    Args:
        a (int): _Any valid integer_
        b (int): _Any valid integer_

    Returns:
        int: the result of the multiply
    """
    return a * b


print(multiply())
