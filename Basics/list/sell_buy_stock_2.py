"""
In this  case 1 stock buy can depends on you
"""

prices = [7,1,5,3,4,6]

profit = 0
n = len(prices)

for i in range(n-1):
    if prices[i+1] > prices[i]:
        profit += prices[i+1] - prices[i]
    

print(profit)