# find X to the power n

def findPow(x,n):
    # base case
    if n == 0:
        return 1
    # recursive case
    a = findPow(x, n//2)
    
    if n % 2 == 0 :
        return a * a
    else:
        return a * a * x
    
def MyPow(x,n):
    if n >= 0:
        return findPow(x,n)
    else:
        return 1 / findPow(x, n*(-1))
    
print(MyPow(2,5))