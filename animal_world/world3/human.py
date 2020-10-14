import animal
import world

class Human(animal.Animal):
    def __init__(self, world, name):
        super().__init__(world, name)
    
    def identify(self):
        print ("Hello, I'm an human named {}".format(self.name)) 
    