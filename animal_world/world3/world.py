import animal

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
    