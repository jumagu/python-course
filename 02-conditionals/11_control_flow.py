# Control the flow of the program with desicion making by using conditions

age = input("Insert your age: ")

age = int(age)

if age < 0:
    print("Age cannot be negative.")
elif age <= 12:
    print("You are a kid.")
elif age <= 17:
    print("You are an adolescent.")
elif age <= 64:
    print("You are an adult.")
else:
    print("You are robbering oxigen!")
