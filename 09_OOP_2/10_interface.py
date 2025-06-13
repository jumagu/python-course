# Interface is a contract that defines how a class must look like
from abc import ABC, abstractmethod


class Animal(ABC):
    # Absctact method is a method that its declared but not implemented in the base class
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        print("zzzz....")


class Dog(Animal):
    def sound(self):
        return "Whoof! Whoof!"

    def sleep(self):
        return super().sleep()


class Cat(Animal):
    def sound(self):
        return "Meow! Meow!"

    def sleep(self):
        return super().sleep()


dog = Dog()
cat = Cat()

dog.sleep()
cat.sleep()
