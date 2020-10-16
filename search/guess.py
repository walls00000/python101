import random
number = random.randint(1,20)
guess = 0
print("I'm thinking of a number from 1 to 20. What is it?")
user_input = input()
print("type = ", type(user_input))
print("isinstance = ", isinstance(user_input, int))
if type(user_input) == int:
  # Notice this block is never executed because the cast to type int is not done
  print("user_input was an integer")
else:
  # user_input is always type <class 'str'> . . . not an integer
  print("user_input was NOT an integer")

## In order to check the type, we need something called a try block.
## In a try block we try to do something risky, and in the case it 
## doesn't work ('except' key word) we code what we want to do if 
## things don't go as intended.
try:
  guess = int(user_input)
  print("user input was an integer")
except ValueError:
  print("Non-integer input detected")
