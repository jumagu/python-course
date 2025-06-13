# It consists of the property that classes can encapsulate logic and properties so that they can only be seen from the class itself, and not from the outside. This is an important property for the security of the systems.


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)

print("Balance:", account.get_balance())
