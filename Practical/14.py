class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print('amount must be positive')
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            print("insuficint balance")
    
    def get_balance(self):
        return self._balance
    
account = BankAccount(12345678, 5000)
account.deposit(2000)
account.withdraw(1000)
print(account.get_balance())

            
