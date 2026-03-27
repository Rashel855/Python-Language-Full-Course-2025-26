# Define a Employee class with attributes role, department & salary. This class also have showDetails() method
# Create an Engineer class that inherits the properties from the Employee & has additional attributes: name & age

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print("role = ", self.role)
        print("department = ", self.dept)
        print("salary", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Accountant", "IT", "75,000")
    def showDetails(self):
        # print("role = ", self.role)
        # print("department = ", self.dept)
        # print("salary", self.salary)
        print("Engineer name = ",self.name)
        print("Engineer age =", self.age)
    
# e1 = Employee("Accountant", "Finance", "60,000")
# e1.showDetails()

eng1 = Engineer("Elon Musk", 40)
eng1.showDetails()