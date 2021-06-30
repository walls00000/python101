## Define the blueprint for what a person is
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(this_self_object_can_be_called_anything_but_it_must_be_first):
        print("Hello, my name is {}, my age is {}".format(this_self_object_can_be_called_anything_but_it_must_be_first.name, this_self_object_can_be_called_anything_but_it_must_be_first.age))
        

## Create some object instances of Person
p1 = Person("Ava", 12)
p2 = Person("Anya", 18)

## Show the properties of this object
p1.show()
p2.show()