tax = 16


def change_global():
    global tax  # * Special keyword that allow to access global app context and modify global variable values
    tax = 18
    return tax


print(change_global())
print(tax)
