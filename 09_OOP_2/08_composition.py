# Composition > Multiple Inheritance


class Flyer:
    def fly(self):
        print("I can fly.")

    def do_something(self):
        print("Do something flyer.")


class Swimmer:
    def swim(self):
        print("I can swim.")

    def do_something(self):
        print("Do something swimer.")


class Duck:
    def __init__(self):
        # ? Composition consist on create instances of the classes as a properties of the class is compositioning, this approach give more control by allowing to use the things needed only instead of directly inherit all the property of the other classes.
        self.flyer = Flyer()
        self.swimmer = Swimmer()

    def quack(self):
        print("Quack Quack!")

    def start_fly(self):
        self.flyer.fly()

    def start_swim(self):
        self.swimmer.swim()


donald = Duck()
donald.start_fly()
donald.start_swim()
donald.quack()

# * MRO (Method Resolution Order)
print(Duck.__mro__)
