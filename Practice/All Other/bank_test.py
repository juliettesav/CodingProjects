class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner 
        self.balance = balance 

    def deposit(self):
        deposit_amt = int(input("How much would you like to deposit? "))
        self.balance = self.balance + deposit_amt 
        return self.balance

    def withdraw(self):
        withdraw_amt = int(input("How much would you like to withdraw? "))
        self.balance = self.balance - withdraw_amt
        return self.balance

bank = BankAccount("Juliette", 500)

print(bank.deposit())
print(bank.withdraw())