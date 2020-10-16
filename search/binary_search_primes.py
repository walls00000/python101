import random
low = 0
high = 24
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
random_index = random.randint(low, high)
number = primes[random_index]

count = 0;
while(True):
    count += 1
    if low <= high:
        i = int((low + high) / 2)
        if primes[i] == number:
            print("Guessed number {} in {} tries".format(number, count))
            break
        elif primes[i] < number:
            low = i + 1
        else:
            high = i - 1
    else:
        print("Failed to find {} after {} tries".format(number, count))
        break;
    