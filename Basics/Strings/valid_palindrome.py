# This problem can solve in 2 ways.
# We solve in both ways.

# 1st method ---> reverse the string and compare
s1 = "nayan"
rev_s1 = s1[::-1]

if s1 == rev_s1:
    print("Palindrome")
else:
    print("Not Palindrome")
    
# 2nd method ---> check both side char if same it's  palindrome 

s2 = "malayalam"

i = 0
j = len(s2)-1

while i<j:
    if s2[i] != s2[j]:
        print("Not Palindrome")
        break
    
    i += 1
    j -= 1
else:
    print("Palindrome")
    
# 