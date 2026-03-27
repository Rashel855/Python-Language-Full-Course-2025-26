# print(1 + 2) #3
# print("Rashel" + " Mahmud")# Concatenate
# print([1, 2, 3] + [4, 5, 6])#Merge

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#     def showCplxNum(self):
#         print(self.real, "i + ", self.img, "j")
#     def add(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1, 3)
# num1.showCplxNum()

# num2 = Complex(4, 5)
# num2.showCplxNum()

# num3 = num1.add(num2)
# num3.showCplxNum()


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showCplxNum(self):
        print(self.real, "i + ", self.img, "j")

        # Using Dunder function
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showCplxNum()

num2 = Complex(4, 5)
num2.showCplxNum()

num3 = num1+ num2
nuu4 = num3-num2
num3.showCplxNum()
nuu4.showCplxNum()