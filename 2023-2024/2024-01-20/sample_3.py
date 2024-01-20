class bank:
    def __init__(self, initial_deposit=0):
        self.balance = initial_deposit
    
    def deposit(self, amount):
        # <what happens when you deposit>
        self.balance += amount
        # self.balance = self.balance + amount
    
    def withdraw(self, amount):
        self.balance -= amount
        # self.balance = self.balance - amount
    
    def check_balance(self):
        print(f"The current balance: {self.balance}")

b1 = bank()
print("After the bank account is created")
print(b1.check_balance())

b1.deposit(amount=1)
print("After the deposition")
print(b1.check_balance())

b1.withdraw(amount=1)
print("After the withdraw")
print(b1.check_balance())

b2 = bank(initial_deposit=100)
print(b2.check_balance())

b3 = bank(initial_deposit=1000)
print(b3.check_balance())
