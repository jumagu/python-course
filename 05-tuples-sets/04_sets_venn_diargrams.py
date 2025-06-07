set1 = {1, 2, 3}
set2 = {4, 5, 6}

# Union
# Return a new set with elements from the set and all others.
set_union = set1.union(set2)

print(set_union)

# Intersection
# Return a new set with elements common to the set and all others.
set3 = {3, 4, 5, 6, 7}
set4 = {7, 7, 1, 2, 5, 6, 4}
set_intersection = set3.intersection(set4)

print(set_intersection)

# Difference
# Return a new set with elements in the set that are not in the others
set_difference = set3.difference(set4)
print(set_difference)

# Other important thing, you can pass more than 1 set in union(), intersection(), difference()

set_multi_union = set1.union(set2, set3, set4)
print(set_multi_union)
