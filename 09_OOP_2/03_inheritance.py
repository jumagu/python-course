# Inheritance can be seen as the family inheritance. It consist in the idea that a father class pass its properties and methods to a class that inherit from.


class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def dog_sound(self):
        print(f"{self.name} says Guau!")


class Cat(Animal):
    def cat_sound(self):
        print(f"{self.name} says Guau!")


cat = Cat("Misifu")
cat.sleep()

dog = Dog("Roko")
dog.sleep()
dog.dog_sound()
