import random
low = 0
high = 24
random_index = random.randint(low, high)
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
number = primes[random_index]

for i in range(low, high):
    if number == primes[i]:
        print("Found {} in {} try(s)".format(number, i+1))
        break
    
    
