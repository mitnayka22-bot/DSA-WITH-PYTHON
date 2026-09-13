# Print 1 to N using Recursion

def PrintNum(i,n):
    if i>n:
        return
    
    print(i, end=" ")
    return PrintNum(i+1, n)

PrintNum(1, 5)