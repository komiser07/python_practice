class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете")
        self._balance -= amount

    def get_balance(self):
        return self._balance

account = BankAccount(100)
account.deposit(10)
account.withdraw(40)
print(account.get_balance())