class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance=self.balance + amount
        print(self.balance)
        return self
    def withdraw(self, amount):
        if self.balance<amount:
            self.balance=self.balance-5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance=self.balance-amount
            print(self.balance)
        return self
    def display_account_info(self):
        print(f"balance:{self.balance}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance=self.balance+(self.balance* self.int_rate)
            print(self.balance)
        else:
            print("balance is nigative")
        return self

alex=BankAccount(0.1,500)
monji=BankAccount(0.1,1000)
alex.deposit(100).deposit(100).deposit(100).withdraw(700).yield_interest().display_account_info()
monji.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()