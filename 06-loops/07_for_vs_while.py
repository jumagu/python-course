# For vs While

# ? For: is desined to iterate iterables
# ? While: is designed to execute code indefinitely while a condition is true

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)

print("========")

item = 0
while item < len(my_list):
    item += 1
    print(item)
