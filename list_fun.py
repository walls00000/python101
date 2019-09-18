#!/usr/bin/python
from __future__ import print_function
import random

woman = ["A scientist", "A queen", "A pirate", "A giant rabbit"]

man = ["a police officer", "an artist", "your grandfather", "a robot"]

place = ["on Pluto.", "at the supermarket.", "in a spooky, bat-filled cave."]
sheWore = ["scuba diving gear.", "fairy wings.", "a paper bag"]
heWore = ["a purple suit.", "a shark costume.", "a beach towel."]
womanSays = ["'Who are you?'", "'How many beans make five?'", "'Why?'"]
manSays = ["'Beep boop!'", "'Don't eat frogs!'", "'What time do you call this?'"]
consequences = ["world peace.", "chaos.", "a giant foot squashed them.", "rainbows."]
worldSaid = ["'Utter nonsense!'", "'Cheese is trending now.'", "'I'm melting!'"]

control = ""
while control != 'exit':
    print(random.choice(woman), "met", random.choice(man), random.choice(place))
    print("She was wearing", random.choice(sheWore))
    print("He was wearing", random.choice(heWore))
    print("She said,", random.choice(womanSays))
    print("He said,", random.choice(manSays))
    print("The consequence was", random.choice(consequences))
    print("The world said,", random.choice(worldSaid))
    print()
    control = raw_input("Press enter to play again. 'exit' to stop) . . . ")
    print()

