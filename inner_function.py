class Calculator:
    def __init__(self, number):
        self.number = number

    def operate(self, operation):
        # Inner function defined inside 'operate'
        def square(n):
            return n * n

        def cube(n):
            return n * n * n

        def double(n):
            return n * 2

        if operation == 'square':
            return square(self.number)
        elif operation == 'cube':
            return cube(self.number)
        elif operation == 'double':
            return double(self.number)
        else:
            return "Invalid operation"


#  Create object
calc = Calculator(5)

# Call inner function through outer method
print("Square:", calc.operate('square'))   # Output: 25
print("Cube:", calc.operate('cube'))       # Output: 125
print("Double:", calc.operate('double'))   # Output: 10
