# Enumerate helps us to get the index of the iterable
for index, char in enumerate("DevTalles"):
    print(index, char)

for index, el in enumerate(["Michigan", "Sahara", "wireless", "Cotton"]):
    print(index, el)

for index, el in enumerate(list(range(100))):
    print(index, el)
