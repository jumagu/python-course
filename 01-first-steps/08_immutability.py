"""
Immutability in programming is a concept where data or objects
cannot be modified after they have been created. Once
defines an immutable value, it remains constant throughout its existence
in the program.
"""

# Un ejemplo de objetos inmutables en python, lo strings:

name = "Juan"
name = "Manuel"  # Re-asignamos el valor de name

name[0] = "S"

"""
Do not confuse immutability with not being able to reassign the value to the variable.
These are two different things. A variable may have an immutable value, but that does not make it a constant.
What it means is that the value cannot be modified, but it still can be reassigned.
"""
