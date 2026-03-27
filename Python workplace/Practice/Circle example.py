# Define a Circle class to create a circle with radius r using the constructor
# Define an Area() method of the class which calculates the area of the circle
# Define Perimeter() method of the class which calculate the perimeter of the circle


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        self.area = (22/7) * (self.radius)**2
        print("The area of the circle is: ", self.area)

    def perimeter(self):
        self.perimeter = 2 * (22/7) * self.radius
        print("The perimeter of the circle is: ", self.perimeter)

c1 = Circle(21)
c1.area()
c1.perimeter()