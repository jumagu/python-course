class Person:
    # ? Global or class attributes
    specie = "Human"

    # Attributes are characteristics of the class, of the real like entity we are representing in code
    def __init__(self, name, age):
        # ? Public instance attributes
        self.name = name  # Instance attributes
        self.age = age

    # ? Public method
    def work(self):
        return f"{self.name} is working hardly."

    def eat(self, food: str):
        if food.lower() == "tacos":
            return "SUPERPOWERS"
        else:
            return "+Energy"


person1 = Person("Juan", 22)

# Public attributes are accesible ouside of the class
print(person1.name)
print(person1.age)
print(person1.specie)

print(person1.work())

print(person1.eat("Hot Dog"))
