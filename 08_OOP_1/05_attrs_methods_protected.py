class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._energy = 100  # ? underscpre indicates it's a protected attribute.

    # ? Methods can aslo be protected
    def _waste_energy(self, quantity):
        self._energy -= quantity


"""
Protected methods and attributes are still accesible by instances outside and are shared on inheritance, different from other languages like java.
"""

"""
Access level of attributes an methods are purely for develoment purposes. It is to write more understandable, maintainable code, helping other developers understand that code.
"""


person1 = Person("Juan", 22)
print(person1.name)
print(person1._energy)
person1._waste_energy(10)
print(person1._energy)
