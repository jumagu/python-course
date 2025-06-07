students = {"Ana": [8, 7, 9], "Luis": [6, 5, 7], "Sofia": [10, 9, 10]}

students["Juan"] = [10, 10, 10]

name = "Ana"
result = ""

if name in students:
    grades = students[name]
    average_grade = sum(grades) / len(grades)

    if average_grade >= 6.0:
        result = f"{name} successfully approve performing a global grade of {average_grade:.1f}"
    else:
        print("{name} failed.")
else:
    result = f"Student {name} is not in the dict"

print(result)
