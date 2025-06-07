# Symmetric difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Return a new set with elements in either the set or other but not both.
# It is like the counterpart of the intersection
set_symmetric_diff = set1.symmetric_difference(set2)

print(set_symmetric_diff)

# Is Subset
set1 = {1, 2}
set2 = {1, 2, 3, 4}

is_subset = set1.issubset(set2)

print(is_subset)  # True

is_subset = set2.issubset(set1)

print(is_subset)  # False

# Is Superset
is_superset = set1.issuperset(set2)

print(is_superset)  # False

is_superset = set2.issuperset(set1)

print(is_superset)  # True
