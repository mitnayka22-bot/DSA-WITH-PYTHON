accounts = [[3,7],[4,9],[3,8]]
ans = 0 
for account in accounts:
    ans = max(ans,sum(account) )
    # print(ans)
print(ans)