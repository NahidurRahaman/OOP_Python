# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person Constructor: Name - {self.name}, Age - {self.age}")

# Derived class from Person
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  
        self.employee_id = employee_id
        print(f"Employee Constructor: ID - {self.employee_id}")

# Derived class from Employee
class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)  
        self.department = department
        print(f"Manager Constructor: Department - {self.department}")

# Create a Manager object
m1 = Manager("Nahid", 28, "EMP123", "IT")
