# A constructor is the first thing that is executed when an instance of the class is created.


class Person:
    # ? Constructor is a special method function
    def __init__(self, name, age):  # Self refers to the object itself
        # Class Attributes
        # It is possible to create and assing its value in the constructor
        self.name = name
        self.age = age
