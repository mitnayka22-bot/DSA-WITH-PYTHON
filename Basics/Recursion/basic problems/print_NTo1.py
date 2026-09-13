def print_Nto1(i,n):
    # base case
    if i>n:
        return
    # recursive case 
    print_Nto1(i+1, n)
    print(i, end=" ")

print_Nto1(1,10)

