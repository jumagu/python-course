class Flyer:
    def fly(self):
        print("I can fly.")

    # ? What happens when two or more classes have the same name and another class inherit from them?
    def do_something(self):
        print("Do something flyer.")


class Swimmer:
    def swim(self):
        print("I can swim.")

    def do_something(self):
        print("Do something swimer.")


class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack Quack!")


donald = Duck()
donald.fly()
donald.swim()
donald.quack()
donald.do_something()  # ? Calls the method of the first inherited class

# * MRO (Method Resolution Order)
print(Duck.__mro__)
