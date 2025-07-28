class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __add__(self, other):
        
        return BankAccount(self.owner + " & " + other.owner, self.balance + other.balance)

    def __sub__(self, other):
        
        return BankAccount(self.owner + " - " + other.owner, self.balance - other.balance)

    def __repr__(self):
        return f"{self.owner}: ${self.balance}"


acc1 = BankAccount("Alice", 5000)
acc2 = BankAccount("Bob", 3000)

total_acc = acc1 + acc2
diff_acc = acc1 - acc2

print(total_acc)   
print(diff_acc)    
