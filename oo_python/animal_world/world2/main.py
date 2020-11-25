import animal
import world


world = world.World()

animal1 = animal.Animal(world, "Fred")
animal2 = animal.Animal(world, "Barny")
animal3 = animal.Animal(world, "Allice")

world.moveAnimals()
world.identifyAnimals()

