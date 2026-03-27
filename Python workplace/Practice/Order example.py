# Create a class called Order which store item & its price
# Use Dunder function __gt__()to convey thata:
# order1> order2 if price of order1> price of order2

class Order:
    def __init__(self, item, price):
        self. item = item
        self.price = price
    def __gt__(self, order2):
        return self.price>order2.price
    
o1 = Order("tomato", 50)
o2 = Order("potato", 40)  

print("The order1 is big",o1>o2)