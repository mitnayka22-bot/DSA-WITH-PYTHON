# Find maximum profit - Best time to sell and buy stock

prices = [7,1,3,5,2,6]

min_price = prices[0]
profit = 0
n = len(prices)
for i in range(1,n):
    curr_profit = prices[i] - min_price
    
    if curr_profit > profit:
        profit = curr_profit
        
    # minimum price
    min_price = min(min_price, prices[i])

print(profit)