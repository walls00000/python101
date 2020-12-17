class World:
   
    def __init__(self):
          self.animals = [];
          
    def addAnimal(self, animal):
       print("Adding {} to world".format(animal.name))
       self.animals.append(animal)
    
    def moveAnimals(self):
        for animal in self.animals:
            animal.move();
          
    def identifyAnimals(self):
        for animal in self.animals:
            animal.identify()   

class Animal:
    
    def __init__(self, world, name):
        self.world = world
        self.name = name
        self.world.addAnimal(self)
    
    def identify(self):
        print ("Hello, I'm an animal named {}".format(self.name)) 
           
    def move(self):
        print("{} is moving".format(self.name))

world = World()

animal1 = Animal(world, "Fred")
animal2 = Animal(world, "Barny")
animal3 = Animal(world, "Alice")

world.moveAnimals()
world.identifyAnimals()