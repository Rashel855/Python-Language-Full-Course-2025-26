class Student:
    def __init__(self, name, marks):
        print("Adding new student in database....")
        self.name = name
        self.mark = marks

s1 = Student("Rashel Mahmud", 99)
print(s1.name, s1.mark)

s2 = Student("Nahid Islam", 89)
print(s2.name, s2.mark)