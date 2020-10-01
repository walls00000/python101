woman = ["a dinosaur", "a brachiosaurus", "a vegetarian"]
man = ["a dinosaur", "tyrannosaurus rex", "a carnivore"]
place = ["at jurassic world", "in restaurant", "at Dino Dinner"]
sheWore = ["a flower hat", "a leaf dress", "a eat more kale shirt"]
heWore = ["a brachiosaurus leather jacket", "ankylosaurus pants", "velociraptor teeth necklace"]
womanSays = ["I would like a cesar salad", "I would like a small orange juice", "I would like a vegin ice-cream"]
manSays = ["Get me a large stegosaurus stew", "Get me a spinosaurus chowder with extra spines", "Get me pterodactyl wing noodles"]
consequence = ["allosaurus charged into the restaraunt hungary for some dinosaurs", "allosaurus barges into the restaraunt only finding his worst enemy the T-rex", "allosaurus enters and finds his worst enemy the T-rex"]
worldSaid = ["FLEE TO ANOTHER PLANET!", "AHHHHHHH", "ALLOSAURUS IS GOING TO EAT US!"]
import random
while True:
    print(random.choice(woman), "met", random.choice(man), random.choice(place))
    print("She was wearing", random.choice(sheWore))
    print("He was wearing", random.choice(heWore))
    print("She said,", random.choice(womanSays))
    print("He said,", random.choice(manSays))
    print("The consequence was", random.choice(consequence))
    print("The world said,", random.choice(worldSaid))
    print()
    input("press enter to play again (<ctrl-c> to quit).")
    print()

