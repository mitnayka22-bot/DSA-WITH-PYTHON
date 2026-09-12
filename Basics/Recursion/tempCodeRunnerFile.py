def factN(n):
    # base case
    if n<=1:
        return 1
    
    # recursive case
    factn = factN(n)
    factNm1 = factN(n-1)
    return factn * factNm1

print(factN(5))