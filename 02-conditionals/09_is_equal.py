# What's the difference between 'is' operator and '==' operator

# Compares the value only, not if the same reference in memory
# print(5 == 5)  # True
# print(True == 1)  # True
# print("" == 1)  # False
# print([] == 1)  # False
# print(10 == 10.0)  # True


new_list = []
other_list = []

print(new_list == other_list)  # True

# Compares if two values point to the object in memory
# Verifies is they have the same identity
print(new_list is new_list)  # False
