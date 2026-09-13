def Num_sum(n):
    
    # base case
    if n == 0:
        return 0    
    # recursive case
    return n + Num_sum(n-1)

print(Num_sum(4))