# This approach for only sorted array 
# We not use dict 
# Solve using two pointers

arr = [2,3,8,11,20,35,52]
left = 0
right = len(arr) - 1
target = 23
while left < right:
    sum1 = arr[left] + arr[right]
    if sum1 == target:
        print([left, right])
        break
    elif sum1 > target:
        right -= 1
    else:
        left += 1