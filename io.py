#!/usr/bin/python

###############################
## In python 2.x the print function is a special statement and print will work with differing results.
## To use a real print() function, import one from python3.x.  This will normalize the output.
###############################
#from __future__ import print_function

###############################
## In Python 2.X input will try to evaluate the input.  
## If this behavior is not desired, use raw_input()
## name=input("What is your name?")
## print("Hello ", name)
###############################

print("Create your character!")
name = input("What is your character called? ")
age = input("How old is your character? ")
strengths = input("What are your character's strengths? ")
weaknesses = input("What are your character's weaknesses?" )

print("Your character's name is ", name)
print("Your character's age is ", age)
print("Strengths: ", strengths)
print("Weaknessess: ", weaknesses)
print(name, " says, 'Thanks for creating me!'")
