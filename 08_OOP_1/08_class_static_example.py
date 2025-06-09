# Example using @classmethod and @staticmethod


class BankAccount:
    interest_rate = 0.02

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print("Interest rate changed")

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def withdraw(self, amount):
        if not self.validate_amount(amount):
            print("Invalid amount.")
            return
        if not self.balance >= amount:
            print("You do not have enouth balance.")
            return
        self.balance -= amount
        print("Success withdraw.")


account1 = BankAccount("Juan", 2000)
account2 = BankAccount("Maria", 3500)

print(BankAccount.interest_rate)

BankAccount.change_interest_rate(0.03)

print(BankAccount.interest_rate)

account1.withdraw(1500)
account2.withdraw(4000)
