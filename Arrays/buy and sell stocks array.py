#given a list of Prices we need to find the max profit such that u buy and sell stock , cannot sell before buying 
from typing import List
def buyandsell(self, prices:List[int])->int:

    if len(prices) == 0:
        return 0 

    max_profit = 0
    min_price = prices[0]

    for price in prices:
        if price < min_price:
            min_price = price
        elif price-min_price > max_profit:
            max_profit = price - min_price
        
    return max_profit


    