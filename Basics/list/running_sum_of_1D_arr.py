"""
input = [1,2,3,4]
output = [1,3,6,10]
"""
nums = [1,2,3,4]

n = len(nums)

ans = []
ans.append(nums[0])

for i in range(1, n):
    x = ans[i-1] + nums[i]
    ans.append(x)
    
print(ans)