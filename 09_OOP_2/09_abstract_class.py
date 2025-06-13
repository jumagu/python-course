# Abstract classes cannot be instantiated
# Abstract serve as a template only

# Abstract Base Class module
from abc import ABC, abstractmethod


class Animal(ABC):
    # Absctact method is a method that its declared but not implemented in the base class
    @abstractmethod
    def sound(self):
        pass

    def sleep():
        print("zzzz....")


animal = Animal()
