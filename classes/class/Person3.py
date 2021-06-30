## Define the blueprint for what a person is
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print("Hello, my name is {}, my age is {}".format(self.name, self.age))
        

## Create some object instances of Person
p1 = Person("Ava", 12)
p2 = Person("Anya", 18)

## Show the properties of this object
p1.show()
p2.show()