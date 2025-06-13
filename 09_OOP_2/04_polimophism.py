class Animal:
    def make_sound(self):
        print("Animal Sound!")


class Dog(Animal):
    def make_sound(self):
        print("Whoof Whoof!")


class Cat(Animal):
    def make_sound(self):
        print("Miau Miau!")


def make_noise(animal):
    if isinstance(animal, Animal):
        animal.make_sound()
    else:
        print(f"{animal} is not an Animal")


make_noise(Dog())
make_noise(Cat())
make_noise("Hola Mundo")
