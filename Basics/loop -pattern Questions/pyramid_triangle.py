"""Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

    *
   ***
  *****
 *******
*********

Print the pattern in the function given to you."""

n = 4 

for i  in range(1, n+1):
    # for spaces
     for j in range(1, n-i+1):
         print(" ", end=" ")
     # for stars
     for k in range(1, 2*i):
         print("*", end=" ")
     print()