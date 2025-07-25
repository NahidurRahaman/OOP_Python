class Student:
    def __init__(self, name):
        self.name = name
        self.has_attended = False
        self.marks = 0

    def attend_to_exam(self):
        print(f"{self.name} has attended the exam.")
        self.has_attended = True

    def get_marks(self):
        if self.has_attended:
            import random
            self.marks = random.randint(50, 100)  # Random mark between 50 to 100
            print(f"{self.name} got {self.marks} marks.")
        else:
            print(f"{self.name} did not attend the exam, so no marks.")


student1 = Student("Nahid")
student2 = Student("Rafi")

student1.attend_to_exam()
student1.get_marks()

student2.get_marks()  
