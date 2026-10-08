arr = [3,3,5,7,7,7,7,9,9,12,12]

n = len(arr)
start = 0

for i in range(1,n):
    # unique elements
    if arr[i] != arr[start]:
        start += 1  
        arr[start] = arr[i]

print(arr[:start+1])  # [3, 5, 7, 9, 12]
print(f"Length : {start+1}")