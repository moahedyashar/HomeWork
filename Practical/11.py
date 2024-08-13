class Account:
    def __init__(self, balance = 0):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("deposit amount must be positive")

    def withdrawal(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            print("insufficient balance")

    def get_balance(self):
        return self._balance
    
account = Account(0)

account.deposit(50)
account.withdrawal(49)
print(account.get_balance())