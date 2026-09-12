n = 4
for i in range(1, n+1):
    # left side number triangle
    for j in range(1, i+1):
        print(j, end=" ")
    
    # for spaces -> (n-i)*2
    for k in range((n-i)*2):
        print(" ",end=" ")
    
    # right side number triangle
    for m in range(i, 0, -1):
        print(m, end=" ")
    
    print()
    