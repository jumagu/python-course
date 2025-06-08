# An iterable is an object that can be iterated
# An iterator is a

# ? Iterables: Lists, Dictionaries, Sets, Tuples
numbers = [1, 2, 3, 4, 5]

# ? Iterator: an iterable that remember its current iteration value and position
iterator = iter(numbers)

print(iterator)
print(next(iterator))
print(next(iterator))

# Iterating a dictionary
user = {"name": "Juan", "age": 22, "can_swim": True}

# By default iterates the keys
for item in user:
    print(item)

for item in user.values():
    print(item)

# Key, value
for key, value in user.items():
    print(key, value)
