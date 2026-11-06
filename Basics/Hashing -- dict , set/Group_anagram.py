strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# sorting fun
def sortString(s):
    s1 = list(s)
    s1.sort()
    return  "".join(s1)

dict1 = {}

for s in strs:
    key = sortString(s)
    # print(key)
    if key in dict1:
        dict1[key].append(s)
    else:
        dict1[key] = [s]

print(list[dict1.values()])