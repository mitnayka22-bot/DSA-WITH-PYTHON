# only one solution of two sum
# do not repeat  any number for two sum 

l1 = [5,1,8,2,6,4,9]
target = 12
n = len(l1)
dict1 = {}

for i in range(n):
    rem = target - l1[i]
    
    if rem in dict1:
        print([dict1[rem], i])
        break
    else:
        dict1[l1[i]] = i
    
"""
Explanation : first create empty dict . 
              find remaning and store in dict with index
              check second element in dict 
              if found then print it and break the loop           
"""