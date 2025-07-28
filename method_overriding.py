class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):  # Method overriding
        return f"Manager: {self.name}, Salary: {self.salary}, Dept: {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def get_details(self):  # Method overriding
        return f"Developer: {self.name}, Salary: {self.salary}, Language: {self.language}"


e1 = Employee("John", 40000)
m1 = Manager("Sarah", 60000, "HR")
d1 = Developer("Mike", 50000, "Python")

for emp in [e1, m1, d1]:
    print(emp.get_details())
