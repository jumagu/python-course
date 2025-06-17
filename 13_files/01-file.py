my_file = open("test_files/test.txt")

# Tead: reads the file content and returns it
print(my_file.read())
print(my_file.read())
print(my_file.read())

# Seek: set the stream position, and return the new stream position.
my_file.seek(0)
print(my_file.read())

# Readline: reads the current line of the file and returns it
print(my_file.readline())

my_file.seek(0)

# Readlines: Return a list of lines from the stream. Starts reading in the current position.
print(my_file.readlines())

my_file.close()
