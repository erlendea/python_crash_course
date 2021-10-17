class Accountant():
    """Manage a bank account."""
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

#erlend = Accountant(500)
#erlend.deposit(200)
#erlend.withdraw(100)
#print(erlend.balance)