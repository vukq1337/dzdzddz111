class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.account = None

    def open_account(self, initial_balance):
        self.account = BankAccount(initial_balance)

    def get_account_balance(self):
        if self.account:
            return self.account.get_balance()
        else:
            return "Клієнт не має банківського рахунку."


class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостатньо коштів на рахунку.")

    def get_balance(self):
        return self.balance

print(dog.name)
print(cat.name)
