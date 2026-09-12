def tribo(n):
    # base case
    if n==0:
        return 0
    if n==1 or n == 2:
        return 1 
    # recursive case 
    return tribo(n-1) + tribo(n-2) + tribo(n-3)

print(tribo(5))