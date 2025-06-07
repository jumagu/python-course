# Convert operations between lists, tuples and sets

list1 = [1, 2, 3, 4, 1, 2, 3, 5, 6, 7, 8, 7, 7, 8, 9]

tuple1 = tuple(list1)
set1 = set(list1)

print(list1)
print(tuple1)
print(set1)

list_tuple = [("a", 1), ("b", 2), ("c", 3)]
dict1 = dict(list_tuple)
print(dict1)
