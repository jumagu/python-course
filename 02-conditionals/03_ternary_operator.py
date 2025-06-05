# Is a way to create a if else statement in another (sometimes cleaner) way

is_student = False

if is_student:
    print("Student Licence")
else:
    print("Free Licence")

print("Student Licence") if is_student else print("Free License")
