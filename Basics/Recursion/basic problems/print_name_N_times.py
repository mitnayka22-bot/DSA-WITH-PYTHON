def print_name(i,n,name,count=0):
    if count==n:
        return
    
    print(f"{i}. {name}")
    return print_name(i+1,n,name, count+1)
    
print_name(1, 10, "Mit")