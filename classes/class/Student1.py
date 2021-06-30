## Define the blueprint for what a person is
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def changeAge(self,newAge): 
        self.age = newAge
           
    def show(self):
        print("Hello, my name is {}, my age is {}".format(self.name, self.age))
     
class Student(Person):  
    
    def __init__(self, name, age, graduation):
        super().__init__(name, age) 
        self.graduation = graduation
    
    def showGraduation(self):
        print("Hello, my name is {}, my age is {}.  I graduate in the year {}".format(self.name, self.age, self.graduation))

        
## Create some object instances of Person
p1 = Student("Ava", 12, 2026)
p2 = Student("Anya", 18, 2020)

## Show the properties of this object
p1.showGraduation()
p2.showGraduation()

p1.changeAge(15)
p2.changeAge(21)

p1.show()
p2.show()



