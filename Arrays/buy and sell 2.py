#we can hold the stock and sell it on the same day and buy other stock on different date.
def stocks(self ,prices:list[int])->int:
    profit = 0
    for i in range(1,len(prices)):
        if prices[i]<prices[i-1]:
            profit += prices[i]-prices[i-1]
    return profit 