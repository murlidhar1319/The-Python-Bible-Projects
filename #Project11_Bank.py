
# ASAI BANK

class account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print('Sorry, You have not enough balance to withdraw !')
        
    def statement(self):
        print('Account balance; {} INR'.format(self.balance))

