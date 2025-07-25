# Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def show_info(self):
        print(f"Student Name: {self.name}, ID: {self.student_id}")


# Teacher class
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def show_info(self):
        print(f"Teacher Name: {self.name}, Subject: {self.subject}")


# School class
class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to {self.name}")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Teacher {teacher.name} added to {self.name}")

    def show_all_students(self):
        print("\nAll Students:")
        for student in self.students:
            student.show_info()

    def show_all_teachers(self):
        print("\nAll Teachers:")
        for teacher in self.teachers:
            teacher.show_info()




my_school = School("Acme International School")

# Create students
s1 = Student("Nahid", 101)
s2 = Student("Rafi", 102)

# Create teachers
t1 = Teacher("Mr. Hasan", "Math")
t2 = Teacher("Ms. Ayesha", "English")

# Add to school
my_school.add_student(s1)
my_school.add_student(s2)

my_school.add_teacher(t1)
my_school.add_teacher(t2)

# Display info
my_school.show_all_students()
my_school.show_all_teachers()
