# Encapsulation
# Wrapping data and functions into a single unit (object).

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