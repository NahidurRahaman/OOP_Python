class Student:
    # Static attribute (class-level)
    university = "DUET"

    def __init__(self, name, dept, gpa):
        self.name = name                  # public attribute
        self._dept = dept                 # protected attribute
        self.__gpa = gpa                  # private attribute
        self.__student_id = self._generate_id()  # private read-only

    # Getter for GPA
    @property
    def gpa(self):
        return self.__gpa

    # Setter for GPA with validation
    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0:
            self.__gpa = value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    # Read-only property (private attribute)
    @property
    def student_id(self):
        return self.__student_id

    # Static method for generating a fake ID
    @staticmethod
    def _generate_id():
        from random import randint
        return f"DUET-{randint(1000, 9999)}"

    # Class method to show university name
    @classmethod
    def get_university(cls):
        return cls.university

    # Instance method
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self._dept}")
        print(f"GPA: {self.__gpa}")
        print(f"Student ID: {self.__student_id}")

s1 = Student("Nahidur", "CSE", 3.85)

# Public attribute
print(s1.name)              # Nahidur

#  Protected attribute (though accessible, not recommended directly)
print(s1._dept)             # CSE

#  Private attribute via getter
print(s1.gpa)               # 3.85

#Update GPA using setter
s1.gpa = 3.95
print(s1.gpa)               # 3.95

#s1.gpa = 4.5     # Raises ValueError

#  Read-only private property
print(s1.student_id)        # DUET-XXXX

# Static method used internally (hidden)
#  Class method
print(Student.get_university())  # DUET

# Instance method
s1.show_info()
