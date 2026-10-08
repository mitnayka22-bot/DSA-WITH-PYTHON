#  max 2 repeated element can use in arr 

nums = [3,3,3,5,2,2,4,4,4,12,12]

n = len(nums)

# if lenght less than 2
if n <= 2:
    print(nums)
    
start = 1
for i in range(2, n):
    if nums[i] != nums[start-1]:
        start += 1 
        nums[start] = nums[i]
        
print(nums[:start+1])   
print(f"Length : {start+1}")