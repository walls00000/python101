#!/usr/bin/python
from __future__ import print_function

print("You are in a dark room in a mysterious castle")

print("In front of you are three doors.  You must choose one.")
playerChoice = raw_input("Choose 1, 2 or 3. . . ")

if playerChoice == "1":
    print ("You find a room full of treasure. You're rich!")
    print ("GAME OVER, YOU WIN!");
elif playerChoice == "2":
    print("The door opens and an angry ogre hits you with his club.")
    print("GAME OVER, YOU LOSE")
elif playerChoice == "3":
    print("You go into the rooj and find a sleeping dragon.")
    print("The dragon wakes up and eats you! You are delicious!")
    print("GAME OVER, YOU LOSE")
else:
    print("Sorry you didn't enter 1, 2 or 3!")
    print("Run the game and try again")
