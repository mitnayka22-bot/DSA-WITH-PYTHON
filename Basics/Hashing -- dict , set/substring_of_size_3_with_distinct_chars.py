#  a String is  good if  there are no repeated charcters
# return number of good substring of length three in s

s = "aababcabc"

n = len(s)
ans = 0

for i in range(n-2): 
    if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i + 2] != s[i]:
        ans += 1

print(ans)