import random
random_index = random.randint(0,19)
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,18,19,20]
number = numbers[random_index]

for i in range(0,19):
    if number == numbers[i]:
        print("Found {} in {} try(s)".format(number, i+1))
        break
    
    
