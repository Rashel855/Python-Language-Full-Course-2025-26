# Create student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average.

# class Student:
#     def __init__(self, name, math, Phy, Chem):
#         self.name = name
#         self.math = math
#         self.Phy = Phy
#         self.Chem = Chem
#     def Get_Avg(self):
#         AVG = (self.math + self.Phy + self.Chem)/3
#         print(AVG)

# s1= Student("Rashel", 99,98,97)
# s1.Get_Avg()


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.mark = marks
    def get_avg(self):
        sum = 0
        count = 0
        for val in self.mark:
            sum+=val
            count+=1
        print("Hi,", self.name, "your average score is: ", sum/count)
    
s1 = Student("Rashel", [99,98,97])
s1.get_avg()        

s1.name = "Rashel Mahmud Rabbi"
s1.get_avg()