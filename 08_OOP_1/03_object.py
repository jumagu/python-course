# A constructor is the first thing that is executed when an instance of the class is created.


class Person:
    # ? Constructor is a special method function
    def __init__(self, name, age):  # Self refers to the object itself
        # Class Attributes
        # It is possible to create and assing its value in the constructor
        # Constructors can contain login inside

        if age >= 18:
            self.name = name
            self.age = age


# An object is an instance of a class

person1 = Person("Juan", 10)

print(person1)
print(person1.name)
print(person1.age)

person2 = Person("Maria", 24)

print(person2)
print(person2.name)
print(person2.age)
