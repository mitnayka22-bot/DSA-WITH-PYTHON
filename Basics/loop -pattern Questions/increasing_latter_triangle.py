"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

A

AB

ABC

ABCD

ABCDE

Print the pattern in the function given to you."""

n = 5

for i in range(1, n+1):
    
    for j in range(1, i+1):
        num = 64+j
        ch = chr(num)
        print(ch, end=" ")
    print()