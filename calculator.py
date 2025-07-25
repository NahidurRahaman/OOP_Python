class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero is not allowed."


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

calc = Calculator(a, b)

print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result:", calc.add())
elif choice == '2':
    print("Result:", calc.subtract())
elif choice == '3':
    print("Result:", calc.multiply())
elif choice == '4':
    print("Result:", calc.divide())
else:
    print("Invalid input")
