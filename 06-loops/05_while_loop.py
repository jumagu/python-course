# Used to execute code WHILE a contidion is met (true)
# We use it when we don't know how many iterations will be needed

# Infinite loop
# while True:
#     pass

counter = 1

while counter <= 10:
    print(f"Count: {counter}")
    counter += 1
else:
    print("Finished")

response = ""

while response.lower() != "python":
    response = input("Type python to quit: ")

print("Finished")
