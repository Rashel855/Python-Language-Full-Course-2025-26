class Student:
    def __init__(self, name, marks):
        self.name = name
        self.mark = marks
        
    @staticmethod       #Decorator
    def hello():
        print("This is the static method..")

    def get_avg(self):
        sum = 0
        count = 0
        for val in self.mark:
            sum+=val
            count+=1
        print("Hi,", self.name, "your average score is: ", sum/count)
    
s1 = Student("Rashel", [99,98,97])
s1.get_avg()        

s1.name = "Rashel Mahmud Rabbi"
s1.get_avg()
s1.hello()