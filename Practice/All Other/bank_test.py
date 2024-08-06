class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner 
        self.balance = balance 

    def deposit(self):
        deposit_amt = int(input("How much would you like to deposit? "))
        balance = balance + deposit_amt 
        return balance

    def withdraw(self):
        withdraw_amt = int(input("How much would you like to withdraw? "))
        balance = balance + withdraw_amt
        return balance

bank = BankAccount("Juliette", 500)

print(bank())