# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person Constructor: Name - {self.name}, Age - {self.age}")

# Base class 2
class Exam:
    def __init__(self, subject, score):
        self.subject = subject
        self.score = score
        print(f"Exam Constructor: Subject - {self.subject}, Score - {self.score}")

# Derived class from both Person and Exam
class Student(Person, Exam):
    def __init__(self, name, age, subject, score, roll):
        Person.__init__(self, name, age)
        Exam.__init__(self, subject, score)
        self.roll = roll
        print(f"Student Constructor: Roll - {self.roll}")

# Create an object
s1 = Student("Nahid", 21, "Math", 95, "CSE-101")
