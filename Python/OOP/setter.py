class BankAccount:
    def __init__(self, balance):
        self._balance = balance


    def set_balance(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = balance


account = BankAccount(100)
print(account.set_balance(200))
account.set_balance(-50)