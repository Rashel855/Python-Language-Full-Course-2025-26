# del keyword

# used to delete object properties or object itself

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rashel Mahmud", 25)
del s1.name
print(s1.age)
print(s1)
del s1
print(s1)