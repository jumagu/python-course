# The reserved word 'with' allow us to manipualte files without the need of closing it at the end
with open("test_files/test.txt", mode="r") as my_file:  # Mode r is read
    print(my_file.readlines())

with open("test_files/test.txt", mode="w") as my_file:  # Mode w is write
    my_file.write(":)")  # Write the file and return the number of characters written

with open(
    "test_files/new_file.txt", mode="w"
) as my_file:  # if the file does not exists, then create it
    my_file.write(":)")

# r+ allow both read and write
with open("test_files/test.txt", mode="r+") as my_file:
    print(my_file.readlines())
    my_file.write("WFT")

# Mode a is append
with open("test_files/test.txt", mode="a") as my_file:
    my_file.write(
        "123456789"
    )  # With mode append, we contact the provided string instead of overrite the file
