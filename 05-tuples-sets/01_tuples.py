# Tuples are like lists, but inmutable
# * Ordered
# * Inmutables
# * Allow duplicates
# * Indexed
my_tuple = (1, 2, 3, 4, "Hola", True, "Hi", 4.5, False)

print(my_tuple)

# Return number of occurrences of value.
print(my_tuple.count(2))

# ! This migth be trikcy because count not only the True values, but also the truthy
print(my_tuple.count(True))

# Return first index of value.
# Just like the array .index().
print(my_tuple.index("Hola"))
