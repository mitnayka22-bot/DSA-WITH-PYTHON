"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
Print the pattern in the function given to you."""

n = 4
for i in range(1, n+1):
    # spaces
    for j in range(1,n-i+1):
        print(" ", end=" ")
        
    # left side
    for k in range(1, i+1):
        num = 64+k
        ch = chr(num)
        print(ch, end=" ")
    # right side
    for m in range(i-1,0,-1):
        num = 64+m
        ch = chr(num)
        print(ch, end=" ")
        
        
    print()