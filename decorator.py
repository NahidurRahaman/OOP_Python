def log_decorator(func):
    def wrapper(*args):
        print(f"Calculating factorial of {args}")
        result = func(*args)
        print(f"Result = {result}")
        return result
    return wrapper

@log_decorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Call the function
factorial(5)
