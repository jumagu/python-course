user = {"name": "Juan", "country": "Colombia", "age": 22}

# ? Copy: Just like the array .copy()
# Return a shallow copy of the dict.
new_user = user.copy()

# ? Pop: simmilar to the arrays .pop(), but require to pass the key to remove
user.pop("country")

print(user)

# ? Popitem: remove the last item, not ususal
user.popitem()

print(user)

# Update
# Very useful method
# Updates the value if exists, create it if not
user.update({"name": "Manuel"})
user.update({"cats": "None"})

# Append
# Very useful hack
user["skills"] = user.get("skills", [])
user["skills"].append("JS")
user["skills"].append("Vue")

print(user)
