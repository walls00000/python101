

def print_primes(number):
    '''print primes starting from number'''
    limit = 100000
    while( number < limit):
        factors = []
        for i in range(1, number+1):
            if number % i == 0:
                factors.append(i)
                # print(i)
        if len(factors) == 2:
            print("{} is prime".format(number))
        number += 1


my_number = int(input("Enter a number: "))
print_primes(my_number)