import random
number = random.randint(1,20)
print("I'm thinking of a number from 1 to 20. What is it?")
count = 0
limit = 6
guess = 0
while count < limit:
  guess = 0
  count += 1
  #guess = int(input())
  user_is_idiot = True
  while user_is_idiot:
    try:
        guess = int(input())
        user_is_idiot = False
    except ValueError:
        print ("YOU IDIOT!! THAT'S NOT A NUMBER  . . . try again ... ")

  print("count = ", count)
  if count == limit:
    print("Have reached the maximum amount of tries!")
    break
  elif guess < number:
    print("Your number was too low...troy, troy again")
  elif guess > number:
    print("Your number was too high, how low can you go...")
  elif guess == number:
    break

if guess == number:
  print("Congradulations! Correct answer!")
else:
  print('You did not guess the number! The number was ' + str(number))