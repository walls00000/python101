def fib(x, y):
    limit = 4000000000
    sum = x + y
    print (sum)
    if(sum < limit):
        fib(y,sum)
        
fib(0, 1)