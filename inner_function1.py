class Calculator:
    def __init__(self, number):
        self.number = number

    def operate(self, operation_func):
        def apply_operation(func):   # Inner function taking function as parameter
            print(f"Applying operation on: {self.number}")
            return func(self.number)

        # Calling inner function and passing external function
        return apply_operation(operation_func)


# External functions (can be passed as arguments)
def square(n):
    return n * n

def cube(n):
    return n * n * n

def double(n):
    return n * 2


# Create object
calc = Calculator(4)

# Pass function as argument to class method
print("Square:", calc.operate(square))    # Output: 16
print("Cube:", calc.operate(cube))        # Output: 64
print("Double:", calc.operate(double))    # Output: 8
