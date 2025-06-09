"""
Class Method
Used to access or modify attributes of the class, instead of the instance. In other words, the class method can be used without the need to create an instance of the class and affect all instances of the class.
"""

"""
Static Method
It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()). Both the class and the instance are ignored, and
neither is passed implicitly as the first argument to the method.

Static methods in Python are similar to those found in Java or C++.
For a more advanced concept, see the classmethod builtin.
"""


class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Class Method
    @classmethod
    def change_specie(cls, new_specie):
        cls.species = new_specie

    # Static Method
    @staticmethod
    def is_adult(age) -> bool:
        return age >= 18


person1 = Person("Juan", 22)
print(person1.species)

# Using class method
Person.change_specie("Humanoid")

person2 = Person("Pepe", 24)
print(person2.species)

# Using static method
old = Person.is_adult(20)  # Without instance
print(old)

print(person1.is_adult(person1.age))  # with the instance
