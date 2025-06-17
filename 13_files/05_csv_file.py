import csv

with open("test_files/data.csv", mode="w", newline="") as my_file:
    writer = csv.writer(my_file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Juan", 22])
    writer.writerow(["Maria", 24])

with open("test_files/data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
