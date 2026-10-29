"""
Check str is valid anagram or not
    When str length is equal
         char are same 
         char freq are same then called anagram string
"""

s1 = "anagram"
s2 = "nagaram"

dict1 = {}
dict2 = {}

for i in s1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1

for i in s2:
    if i not in dict2:
        dict2[i] = 1
    else:
        dict2[i] += 1
        
if dict1 == dict2:
    print("Anagram")
else:
    print("Not anagram")