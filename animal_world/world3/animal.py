import world

class Animal:
    
    def __init__(self, world, name):
        self.world = world
        self.name = name
        self.world.addAnimal(self)
    
    def identify(self):
        print ("Hello, I'm an animal named {}".format(self.name)) 
           
    def move(self):
        print("{} is moving".format(self.name))