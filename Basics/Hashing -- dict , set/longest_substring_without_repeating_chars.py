# find the longest substring in string

s = "abcbacdac"

n = len(s)
set1 = set()
set1.add(s[0])
ans = 1
print(set1)

i = 0
j = 1

while j < n:
    while s[j] in set1:
        set1.discard(s[i])
        i += 1
    set1.add(s[j])
    j += 1
    ans = max(ans, (j-i))

print(ans)