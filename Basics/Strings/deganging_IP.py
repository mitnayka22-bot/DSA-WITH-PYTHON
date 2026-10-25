# IP me . ko replace karo [.]

# 1st Method

address = "1.1.1.1"
print(address.replace(".", "[.]"))

# 2nd Method

address1 = "12.33.44.55"
ans = ""
for i in address1:
    if i != ".":
        ans += i
    else:
        ans += "[.]"
        
print(ans)