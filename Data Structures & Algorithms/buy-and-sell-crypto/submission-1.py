class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_price = prices[0] 
        max_profit = 0
        for price in prices:
            if price< least_price:
                least_price = price
            else:
                profit = price - least_price 
                max_profit = max(profit, max_profit)
        
        return max_profit