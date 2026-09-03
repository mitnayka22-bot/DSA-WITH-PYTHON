"""
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
Print the pattern in the function given to you.
"""

n = 4 

# for upper part of the diamond
for i  in range(1, n+1):

    # for spaces 
    for j in range(1, n-i+1):
        print(" ", end=" ")
        
    # for stars
    for k in range(1, 2*i):
        print("*", end=" ")
    #  for  next line
    print()

# for lower part of the diamond
for i in range(1, n+1):

        # for spaces
        for j in range(1, i):
            print(" ", end=" ")
         # for stars
        for k in range(1, 2*(n-i)+2):
            print("*", end=" ")
        print()