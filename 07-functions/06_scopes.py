# Scope: refers to the context a variable is recognized by the program
# This helps to know where a variable can be used, modified, reassined

global_variable = "Im global"


def other_function():
    enclosing_variable = "Im enclosing"

    def inner_function():
        local_variable = "Im local"

        print(global_variable)
        print(enclosing_variable)
        print(local_variable)

    inner_function()


other_function()
