class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be greater or equal than 18."):
        self.age = age
        self.message = message
        super().__init__(self.message)


class InvalidEmailError(Exception):
    def __init__(self, email, message="Invalid email format."):
        self.email = email
        self.message = message
        super().__init__(self.message)


def register_user(name, age, email):
    if age < 18:
        raise InvalidAgeError(age=age)  # Raise stops the program

    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmailError(email=email)

    print(f"User {name} with email {email} and age {age} successfully registered!")


try:
    register_user("Juan", 18, "juan@test.com")
except InvalidAgeError as e:
    print(e)
except InvalidEmailError as e:
    print(e)
