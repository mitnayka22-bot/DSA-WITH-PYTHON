def fib(n):
    # base case
    if n == 0 or n == 1:
        return n
    
    # recursive case
    return  fib(n-1) + fib(n-2)

print(fib(5))