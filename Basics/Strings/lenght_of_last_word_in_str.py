# in-build and easy method

s = "   fly  me to  the  moon  "

s = s.split()
n = len(s)-1
print(len(s[n]))

# second method using loop

s1 = "   fly  me to  the  moon  "
s1 = s1.strip()
n1 = len(s1)

i = -1
while i>=(-1*n) and s1[i] !=" ":
    i-=1

i+=1
i*=-1

print(i)