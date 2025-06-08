def big_function(*args):
    # Prints a tuple of args
    print(args)
    return sum(args)


# Can pass N number of args of any type
result = big_function(1, 2, 3, 4)

print(result)


def other_function(*args, **kwargs):
    # Prints a tuple of args
    print("args ->", args)

    # Prints a dictionary of args (key - value)
    print("-> kwargs", kwargs)

    kwargs_total = 0

    for value in kwargs.values():
        kwargs_total += value

    return sum(args) + kwargs_total


result = other_function(1, 2, 3, a=1, b=2)

print(result)
