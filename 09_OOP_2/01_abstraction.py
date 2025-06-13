# Abstraction is the fact that Objects only expose the relevant things .. and not the implementation itself, because outside the class it does not matter.

# ? This helps to have a more organized and cleaner code


class CoffeMaker:
    def make_coffe(self):
        self.__boil_water()
        self.__mix()
        print("Your coffe is ready!")

    def __boil_water(self):
        print("Boling water")

    def __mix(self):
        print("Mixing boiled water with coffe")


coffe_maker = CoffeMaker()
coffe_maker.make_coffe()
