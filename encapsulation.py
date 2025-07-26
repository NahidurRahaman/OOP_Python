class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self._account_type = "Savings"   # Protected attribute
        self.__balance = balance    # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    def check_balance(self):
        print(f"Current Balance: {self.__balance}")

# Create object
acc = BankAccount("Nahid", 1000)

# Public access
print("Owner:", acc.owner)  

# Protected access (not recommended directly but possible)
print("Account Type:", acc._account_type)  

# Private access
# print(acc.__balance)  

# Access private using method
acc.check_balance()

# Access private with name mangling (not recommended)
print("Accessing private manually:", acc._BankAccount__balance)  

# Deposit and Withdraw
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()
