class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be greater or equal than 18."):
        self.age = age
        self.message = message

        super().__init__(self.message)


def register_user(name, age):
    if age < 18:
        raise InvalidAgeError(age=age)  # Raise stops the program

    print(f"User {name} with age {age} successfully registered!")


try:
    register_user("Juan", 17)
except InvalidAgeError as e:
    print(e)
