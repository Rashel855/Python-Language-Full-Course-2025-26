# class Student:
#     def __init__(self, phy, math, chem):
#         self.phy = phy
#         self.math = math
#         self.chem = chem
#         # self.percentage = str((self.phy + self.math + self.chem)/3) + "%" #---> way 1
# #     def calcPercentage(self):
# #         self.percentage = str((self.phy + self.math + self.chem)/3) + "%"  #---> way 2
        
# # s1 = Student(89,99,85)
# # print(s1.percentage)

# s1.phy = 90
# s1.calcPercentage()
# print(s1.percentage)

class Student:
    def __init__(self, phy, math, chem):
        self.phy = phy
        self.math = math
        self.chem = chem

    @property
    def percentage(self):
        return str((self.phy + self.math + self.chem)/3) + "%"

s1 = Student(89,99,85)
print(s1.percentage)

s1.phy = 95
print(s1.percentage)