class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     self.__class__.name = name # or Person.name = name
    
    @classmethod 
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rashel Mahmud")
print(p1.name)
print(Person.name)
# Person.name = "Nahid Islam"
# print(Person.name)