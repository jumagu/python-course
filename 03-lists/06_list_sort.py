# List sorting methods
letters = ["b", "o", "h", "k", "u", "e", "g"]

print(letters)

# Sort the list in ascending order and return None.
letters.sort()

print(letters)

# Reversed (descending) sort
letters.sort(reverse=True)

# Return a new list containing all items from the iterable in ascending order.
new_letters = sorted(letters)
print(letters)
print(new_letters)

# other way to reverse a list different from list[::-1]
numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)
