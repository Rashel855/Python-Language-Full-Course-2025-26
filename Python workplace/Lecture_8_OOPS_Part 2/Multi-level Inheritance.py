class Car:   
    acc = False
    brk = False
    clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car is start..")

    def stop(self):
        self.acc = False
        self.clutch = False
        print("Car is stop..")

class ToyotaCar (Car):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        

class Fortuner(ToyotaCar):
    def __init__(self, name):
        self.name = name


car1 = Fortuner("fortuner")
car1.start()
car1.color = "Blue"
print(car1.color)