#The ASCII Quiz Challenge - www.101computing.net/ascii-quiz-challenge
import random

life = 255
score = -1

while life>0:
  print("_______________________________________")
  print("Your life score is " + str(life))
  score+=1
  print("Your score so far: " + str(score))  
  ### Generate Random Character and ASCII value
  #ascii = random.randint(0,127) #Extended ASCII would go up to 255!
  ascii = random.randint(32,126) #Only select printable characters
  character = chr(ascii)
  
  ### Retrieve User Guess
  guess = int(input("What is the ASCII code this charcter: " + character))
  
  ### Update life score
  if guess == ascii:
    print("Correct Answer. Your life score is reset to 255!")
    life = 255
  else:  
    print("Incorrect Answer. The correct answer was " + str(ascii))
    difference = abs(guess-ascii)
    print("You lose " + str(difference) + " life points.")
    life = life - difference
  
print("Game Over!")
print("Your score: " + str(score))