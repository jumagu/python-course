# Double Underscore Methods


class Person:
    # Special funtions/objects/properties in python
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hi, I'm {self.name}"

    def __len__(self):
        return len(self.name)


person = Person("Juan")

# This prints a custom string because of the dunder method __str__
print(person)
# This prints the length of the person name because of the dunder method __len__
print(len(person))
