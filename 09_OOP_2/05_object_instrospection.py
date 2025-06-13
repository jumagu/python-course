# It is like a group functions that allows to see attributes and methods an object have in runtime.

x = [1, 2, 3]

print(type(x))

# Print a list of attrs and methods of x
print(dir(x))

# Return whether the object has an attribute with the given name.
print(hasattr(x, "__len__"))

# Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
# When a default argument is given, it is returned when the attribute doesn't
# exist; without it, an exception is raised in that case.
print(getattr(x, "append"))

# Return whether the object is callable (i.e., some kind of function).
print(callable(x.append))

# Return the identity (Memory location) of an object.
print(id(x))
