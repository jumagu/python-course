# ! Remember that all in python is an object.
# * List are objects, so they have its own special methods

# Addition methods
numbers = [1, 2, 3, 4, 5]

# Append object to the end of the list.
numbers.append(100)

print(numbers)

# Insert object before index.
numbers.insert(1, 200)

print(numbers)

# Extend list by appending elements from the iterable.
numbers.extend([6, 7, 8])

print(numbers)
