# Do not use in-build func and slicing for reverse 

s = ["A", "b","h","i","m","a","n","y","u"]
print(s)
i = 0
j = len(s) - 1

while i < j:
    temp = s[i]
    s[i] = s[j]
    s[j] = temp
    i += 1
    j -= 1

print(s)