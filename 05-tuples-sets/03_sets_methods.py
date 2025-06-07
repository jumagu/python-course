my_set = {1, 2, 3, 5}

print("Original set: ", my_set)

# Add
# Add an element to a set.
my_set.add(4)

print(my_set)

# Remove
# Remove an element from a set; it must be a member.
# If the element is not a member, raise a KeyError.
my_set.remove(1)

print(my_set)

# Dicard
# Remove an element from a set if it is a member.

# ? Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.
my_set.discard(2)
my_set.discard(10)

print(my_set)

# Pop
# ? Delete a random element from the set and returns it
deleted_el = my_set.pop()

print(deleted_el)
