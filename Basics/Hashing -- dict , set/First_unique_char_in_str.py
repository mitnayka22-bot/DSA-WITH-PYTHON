# Given a string s, find the first non-repeating charcter in it and return its index. if it does not exist, return -1

s = "loveleetcode"

freq = {}

for i in s:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
        
print(freq)

n = len(s) - 1

for i in range(n):
    if freq[s[i]] == 1:
        print(f"Char : {s[i]} , idx : {i}" )
        break
    
"""
first count frequence of all char
interate the loop and check all char freq
freq = 1 ---> 1st char that print
"""