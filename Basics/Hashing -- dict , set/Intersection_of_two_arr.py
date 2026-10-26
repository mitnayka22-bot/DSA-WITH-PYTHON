# OutPut must be list/arr

# 1st method 
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

set1 = set(nums1)
set2 = set(nums2)

ans = set1.intersection(set2)
print(list(ans))

# 2nd method --- one line ans

print(list(set(nums1) & set(nums2)))