def sell(prices):
    profit = 0
    minval = prices[0]

    for i in prices:
        minval = min(minval, i)
        profit = max(profit, i - minval)

    return profit

prices = list(map(int, input().split()))
print(sell(prices))