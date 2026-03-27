class Student:
    college_name = "North Bengal International University"
    names = "Anonymous"
    def __init__(self, names, marks):
        self.name = names
        self.mark = marks
        print("Adding New student....")

s1 = Student("Rashel Mahmud", 98)
print(s1.name, s1.mark)