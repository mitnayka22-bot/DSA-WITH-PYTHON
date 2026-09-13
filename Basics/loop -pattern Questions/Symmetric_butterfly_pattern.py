"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
Print the pattern in the function given to you."""

n = 5

# Upper part of pattern

for i in range(1, n+1):
    # left triangle
    for j in range(1, i+1):
        print("*", end=" ")
    
    
    # spaces
    for k in range(1, (n-i)*2+1):
        print(" ", end=" ")
        
    # right triangle
    for m in range(1,i+1):
        print("*",end=" ")
        
    print()

# Lower part  of pattern

for i in range(1, n):
    # left triangle
    for j in range(1, n-i+1):
        print("*", end=" ")
    
    # spaces
    for k in range(1, (i*2)+1):
        print(" ", end=" ")
    
    # right triangle
    for m in range(1, n-i+1):
        print("*", end=" ")
    print()