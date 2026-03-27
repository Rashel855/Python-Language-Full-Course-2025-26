# Super methods

# super() method is used to access methods of the parent class.

class Car:   
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car is start..")

    @staticmethod
    def stop():
        print("Car is start..")

class ToyotaCar (Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

car1 = ToyotaCar("prius", "Electric")
print(car1.type)