def fib_n(n):
    # base case
    if n==1 or n==0:
        return n
    # recursive case 
    return fib_n(n-1) + fib_n(n-2)

print(fib_n(4))