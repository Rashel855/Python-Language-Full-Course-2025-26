class Student:
    college_name = "North Bengal International University"
    names = "Anonymous"
    def __init__(self, names, marks):
        self.name = names
        self.mark = marks
        print("Adding New student....")

    def wel(self):
        print("Welcome!", self.name)
    def get_marks (self):
        return self.mark

s1 = Student("Rashel Mahmud", 98)
s1.wel()
print(s1.get_marks())