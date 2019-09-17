#!/usr/bin/python
from __future__ import print_function
import random

print("You are in a dark room in a mysterious castle")

print("In front of you are three doors.  You must choose one.")
playerChoice = raw_input("Choose 1, 2, 3 or 4. . . ")

if playerChoice == "1":
    print ("You find a room full of treasure. You're rich!")
    print ("GAME OVER, YOU WIN!");
elif playerChoice == "2":
    print("The door opens and an angry ogre hits you with his club.")
    print("GAME OVER, YOU LOSE")
elif playerChoice == "3":
    print("You go into a room full of gold and find a sleeping dragon.")
    print("You can either:")
    print("1) Try to steal some of the dragon's gold.")
    print("2) Try to sneak around the dragon and exit.")
    dragonChoice = raw_input("Type 1 or 2...")
    if dragonChoice == "1":
        dragonWakes = random.randint(0,1)
        if dragonWakes == 1:
            print("The dragon wakes up and eats you! You are delicious!")
            print("GAME OVER, YOU LOSE")
        else:
            print("You are able take some gold and escape the waking dragon!")
            print("Beware next time, the dragon is now awake!")
            print("GAME OVER, YOU WIN (for now)")
    elif dragonChoice == "2":
        print("You sneak around the dragon and escape the castle")
        print("GAME OVER, YOU WIN")
    else:
        print("The dragon wakes up because you entered an incorrect chose!")
        print("He and eats you! You are delicious!")
        print("GAME OVER, YOU LOSE")
elif playerChoice == "4":
    print("You enter a room with a sphinx.")
    print("It asks you to guess what number it is thinking of, between 1 and 10.")
    number = int(raw_input("What number do you choose? "))
    sphinxNumber = random.randint(1,10)
    if number == sphinxNumber:
        print("The sphinx hisses in disapprovement.  You guessed correctly.")
        print("She must lets you go free.")
        print ("GAME OVER, YOU WIN!");
    else:
        print("The sphinx tells you that your guess was incorrect.")
        print("The sphinx was thinking of ", sphinxNumber)
        print("GAME OVER, YOU LOSE")
else:
    print("Sorry you didn't enter 1, 2 or 3!")
    print("Run the game and try again")
