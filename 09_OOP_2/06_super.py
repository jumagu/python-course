class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def info(self):
        print(f"Hi humans! My name is {self.name} and I'm {self.age} yo")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def sleep(self):
        super().sleep()  # super() access to the father method definition


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def sleep(self):
        super().sleep()

    def info(self):
        super().info()
        print(f"My breed is {self.breed}!!")


cat = Cat("Misifu", 3, "Persa")
cat.sleep()
cat.info()
