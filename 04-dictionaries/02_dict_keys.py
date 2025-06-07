# Dictionaries are mutable in Python, just like arrays
# ! Dictionaty keys must be inmutable values, like string, integers or tuples
user = {"name": "Juan", "country": "Colombia", "age": 22}

print(user)

user["age"] = 23
user["country"] = "Switzerland"

print(user)
