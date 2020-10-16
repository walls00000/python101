import random
number = random.randint(1,20)
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,18,19,20]

low = 0
high = 19

count = 0;
while(True):
    count += 1
    if low <= high:
        i = int((low + high) / 2)
        if numbers[i] == number:
            print("Guessed number {} in {} tries".format(number, count))
            break
        elif numbers[i] < number:
            low = i + 1
        else:
            high = i - 1
    else:
        print("Failed to find {} after {} tries".format(number, count))
        break
    