## Define the blueprint for what a person is
class Person:
    
    def __init__(self, name):
        self.name = name

## Create some object instances of Person
p1 = Person("Ava")
p2 = Person("Anya")

## Show the properties of this object
print("p1 =", p1.name)
print("p2 =", p2.name)