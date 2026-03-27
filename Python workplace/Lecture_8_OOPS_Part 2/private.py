# Private (like) attribute & methods
# Conceptual Implementation in Python

# Private attribute & methods are meant to be used only within the class
# and are not accessible from outside the class 

class Account:
    def __init__(self, acc_no, acc_pass):
        # private attribute which can not call outside this class
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def Reset_pass(self,r_acc_pass):
        self.__acc_pass = r_acc_pass
        print(acc1.__acc_pass)

    # private method which can not call outside this class
    def __hello(self):
        print("Hello user!", acc1.acc_no)

    def welcome (self):
        self.__hello()

acc1 = Account("rashel855", "Rashel")

print(acc1.acc_no)
acc1.Reset_pass("Rashel855@")

acc1.welcome()