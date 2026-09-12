def printNum(i,n):
    #base case 
    if i>n:
        return
    # recursive case
    print(i, end=" ")
    printNum(i+1,n)

printNum(1,5)