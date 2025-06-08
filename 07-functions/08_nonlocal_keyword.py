def outer():
    enclosing_var = "Enclosing variable"

    def inner():
        nonlocal enclosing_var  # * nonlocal is simmilar to global but applies to the variables that in a funtion scope
        enclosing_var = "Enclosing modified"

    inner()
    print(enclosing_var)


outer()
