import animal
import human
import world


world = world.World()

animal1 = human.Human(world, "Fred")
animal2 = human.Human(world, "Barny")
animal3 = human.Human(world, "Allice")
animal4 = animal.Animal(world, "Dino")

world.moveAnimals()
world.identifyAnimals()

