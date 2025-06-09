class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__password = "123456"  # double unserscore indicates it's a private attribute. It is a convention.

    # Methods can also be private
    def __generate_password(self):  # Name mangling (_CLASSNAME_password)
        return f"$${self.name}{self.age}"


"""
Private methods and attributes are hided and made unaccesible by instances outside and are NOT shared on inheritance.
"""

"""
Access level of attributes an methods are purely for develoment purposes. It is to write more understandable, maintainable code, helping other developers understand that code.
"""

person1 = Person("Juan", 22)
print(person1.__password)
person1.__generate_password()
print(person1.__password)

# How to access private attributes or methos (DOI NOT DO THIS)
# print(person1._Person__password)
