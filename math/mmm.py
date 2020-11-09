import statistics
from collections import Counter

def mean(numbers):
    return sum(numbers) / len(numbers)

def mean1(numbers):
    return statistics.mean(numbers)

def median(numbers):
    n = len(numbers)
    index = n // 2
    # numbers with an odd number of observations
    if n % 2:
        return sorted(numbers)[index]
    # numbers with an even number of observations
    return sum(sorted(numbers)[index - 1:index + 1]) / 2

def median1(numbers):
    return statistics.median(numbers)

def mode(numbers):
    c = Counter(numbers)
    ## Print the most common and their occurrances in an array
    ## The argument to most_common specifies how many items to
    ## display.  most_common(1) will display the first hit
    #     print("c.most_common(1): {}".format(c.most_common(1)))
    #     print("c.most_common(1)[0][0]: {}".format(c.most_common(1)[0][0]))
    #     print("c.most_common(2): {}".format(c.most_common(2)))
    #     print("c.most_common(3): {}".format(c.most_common(3)))
    
    #     for k,v in c.items():
    #         print("k={} v={}".format(k, v))
    ## Beware of this odd syntax.  We return the key here, but we compare the values
    ## return k if v == c.most_common(1)[0][1] ... value
    #return [k for k, v in c.items() if v == c.most_common(1)[0][1]] 

    for k, v in c.items():
        if v == c.most_common(1)[0][1]:
            return k

def mode1(numbers):
    return statistics.mode(numbers)

#sample = input("numbers: ")
sample = "4 1 2 2 3 5 4 3 4"
array = sample.split()
numeric_array = [int(i) for i in array]
print("sample '{}'".format(numeric_array))

my_mean = mean(numeric_array)
my_median = median(numeric_array)
my_mode = mode(numeric_array)

print("mean: {}".format(my_mean))
print("median: {}".format(my_median))
print("mode: {}".format(my_mode))

my_mean1 = mean1(numeric_array)
my_median1 = median1(numeric_array)
my_mode1 = mode1(numeric_array)

print("mean1: {}".format(my_mean1))
print("median1: {}".format(my_median1))
print("mode1: {}".format(my_mode1))