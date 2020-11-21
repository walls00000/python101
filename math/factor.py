#my_number = 11

def findFactors(number):
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
            # print(i)
    if len(factors) == 2:
        print("number {} is prime".format(number))
    return factors

my_number = int(input("Enter a number: "))
for i in range(1,my_number+1):
    array = findFactors(i)
    print("factors {}: {}".format(i,array))

