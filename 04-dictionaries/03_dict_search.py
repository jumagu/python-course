user = {"name": "Juan", "country": "Colombia", "age": 22, "email": "juan@mail.com"}

print(user["name"])

# Get
# ? Return the value for key if key is in the dictionary, else default.
print(user.get("name", "No name"))

# In
# Search in keys
print("name" in user)

# Get the keys
print(user.keys())

# Get the values
print(user.values())

# Search in values
print("Juan" in user.values())

# Items
# ? Return a set-like object providing a view on the dict's items.
print(user.items())
