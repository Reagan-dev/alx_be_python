# bank_account.py

class BankAccount:
    def __init__ (self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        # add amount to the account balance
        self.account_balance += amount

    def withdraw(self, amount):
        # subtract amount from the account balance
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        # display the current account balance
        print(f"Current balance: ${self.account_balance:.2f}")
