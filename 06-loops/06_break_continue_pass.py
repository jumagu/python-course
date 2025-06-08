# Pass: pass to the next line
for item in [1, 2, 3, 4, 5, 6]:
    pass

# Break
for item in [1, 2, 3, 4, 5, 6]:
    if item == 4:
        break  # Kills the program execution
    print(item)

# Continue
for item in [1, 2, 3, 4, 5, 6]:
    if item == 4:
        continue  # Jumps to the next iteration
    print(item)


num = 0
while num < 50:
    num += 1
    if num >= 10 and num <= 30:
        continue
    print(num)
