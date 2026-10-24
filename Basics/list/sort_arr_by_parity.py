"""
input  = [1,2,3,4]
output = [2,4,1,3]
"""
nums = [3,1,2,4]

n = len(nums)
start = 0
for i in range(n):
    if nums[i] % 2 == 0:
        # Swap the start and current elements
        temp = nums[i]
        nums[i] = nums[start]
        nums[start] = temp
        start += 1
        
print(nums)