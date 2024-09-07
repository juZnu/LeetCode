def maxProfit( prices):
    profit = 0
    min_local = prices[0]
    for i in range(1,len(prices)):
        if prices[i] < prices[i-1]:
            profit += prices[i-1] - min_local
            min_local = prices[i]
    return profit + prices[-1] - min_local

print(maxProfit(prices = [7,1,5,3,6,4]))