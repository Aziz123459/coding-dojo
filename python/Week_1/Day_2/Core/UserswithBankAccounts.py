class BankAccount:
    
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
    



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self,amount):
        self.account.deposit(amount)		
        return self	
    def make_withdrawal (self,amount):
        self.account.withdraw(amount)		
        return self
    def display_user_balance(self):
        self.account.display_account_info()	
        print(self.account.balance)	
        return self




alex=User("alex","alex@gmail.com")
monji=User("monji","monji@gmail.com")
alex.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(300).display_user_balance()
print('#'*10)
monji.make_deposit(100).make_deposit(100).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()