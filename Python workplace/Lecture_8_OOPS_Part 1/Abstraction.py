# Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk  = False
        self.clutch = False
    
    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started")
Car1 = Car()
Car1.start()