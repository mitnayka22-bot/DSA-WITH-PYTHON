"""
print the sum of maximum sub array.
"""

nums = [5,1,-6,3,-5, -3,-9,10,-9,2]
n = len(nums)
curr_sum = 0
max_sum = nums[0]

for i in range(n):
    curr_sum += nums[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
    if curr_sum < 0:
        curr_sum = 0

print(max_sum)
