# You are given an array where each element represents the stock price on that day.
# You can:
#   Buy once
#   Sell once
#   You must buy before you sell
# Return the maximum profit.


def maxProfit(prices):

    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


# optimal solution...
def max_profit(prices):
    min_price=float('inf')
    max_price=0
    for price in prices:
        if price < min_price:
            min_price=price
        profit = price - min_price

        if profit > max_price:
            max_price = profit
    return max_price

prices = [1,4,1,3,2,1]
print(max_profit(prices))