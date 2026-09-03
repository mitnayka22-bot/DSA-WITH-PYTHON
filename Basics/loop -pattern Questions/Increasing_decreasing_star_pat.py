"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


*

**

***

****

*****

****

***

**

*
Print the pattern in the function given to you."""

n  = 4

#  Upper part

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()

# lower part

for i in range(1, n):
    for j in range(1, n-i+1):
        print("*", end="")
    print()