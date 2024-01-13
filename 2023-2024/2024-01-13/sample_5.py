class bank:
    def __init__(self, initial_deposit=0):
        self.balance = initial_deposit
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def check_balance(self):
        print(f"The current balance: {self.balance}")

b1 = bank(initial_deposit=1)
print(f"The balance after opening an account is {b1.balance}")
