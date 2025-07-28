class BankAccount:
    bank_name = "Sonali Bank"  # Static Attribute
    total_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def show_info(self):
        print(f"{self.owner} has balance: {self.balance}")

    @classmethod
    def show_total_accounts(cls):
        print(f"Total Accounts: {cls.total_accounts}")

    @staticmethod
    def validate_amount(amount):
        return amount > 0


acc1 = BankAccount("Nahidur", 5000)
acc2 = BankAccount("Shanto", 7000)

acc1.show_info()
acc2.show_info()

BankAccount.show_total_accounts()   
print(BankAccount.validate_amount(100))  
