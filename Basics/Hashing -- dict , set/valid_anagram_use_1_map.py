"""
Check str is valid anagram or not
    When str length is equal
         char are same 
         char freq are same then called anagram string
"""

s1 = "anagram"
s2 = "nagaram"


if len(s1) != len(s2):
    print("Not anagram")

freq = {}

for i in s1:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
        
for i in s2:
    if i not in freq:
       print("Not anagram")
       break
    else:
        freq[i] -= 1 

for i in freq.values():
    if i != 0:
        print("Not anagram")
        break
else:
    print("Anagram")