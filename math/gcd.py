
def findFactors(number):
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
            # print(i)
    if len(factors) == 2:
        print("number {} is prime".format(number))
    return factors

def gcd(factorlist):
    length1 = len(factorlist[0])
    length2 = len(factorList[1])
    small = factorList[0]
    large = factorList[1]
    if length1 > length2:
        small = factorList[1]
        large = factorList[0]
    for i in range(len(small), 0, -1):
        if (small[i-1] in large):
            return small[i-1]
    return -1 ## should not get here

text = input("Enter two numbers: ")
numbers = text.split()
# print("{} length {}".format(numbers, len(numbers)))
for i in range(0, len(numbers)):
    # print("i: {}".format(i))
    numbers[i] = int(numbers[i])

factorList = []
for i in numbers:
    factors = findFactors(i)
    factorList.append(factors)

print("factors: {}".format(factorList))
my_gcd = gcd(factorList)
print("gcd: {}".format(my_gcd))

