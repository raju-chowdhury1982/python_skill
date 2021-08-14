#practicing how to crreate class(object):

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep):
        self.balance += dep
        return self.balance

    def withdraw(self, wd):
        self.balance -= wd
        return self.balance



acct1 = BankAccount("Mita", 600)
acct2 = BankAccount("Kalpana", 500)

print(acct1.owner, acct1.balance)
print(acct2.owner, acct2.balance)

print(acct1.withdraw(100))
print(acct2.deposit(200))
