# Inheritance 

# when one class (child/derived) derives 
# the properties & methods of another class(Parents/base)

class Car:   
    acc = False
    brk = False
    clutch = False
    brand = "Toyota"
   
    def start(self):
        self.acc = True
        self.clutch = True
        print("Car is start..")

    def stop(self):
        self.acc = False
        self.clutch = False
        print("Car is start..")

class ToyotaCar (Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color


car1 = ToyotaCar("fortuner", "blue")
car2 = ToyotaCar("prius", "red")
car1.start()
print(car1.brand, car1.name, car1. color)