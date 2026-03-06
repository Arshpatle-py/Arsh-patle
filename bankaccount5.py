class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

def deposit(self, amount):
    if amount > 0:
        self.balance += amount
        print(f"₹{amount} deposited successfully.")
        
    else:
        print("Deposit amount must be positive.")

def withdraw(self, amount):
    if amount > 0:
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

        else:
            print("Insufficient balance.")
    else:
        print("Withdrawal amount must be positive.")

def check_balance(self):
    print(f"Current Balance: ₹{self.balance}")