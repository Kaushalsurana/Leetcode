class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price=0
        min_price=float('inf')
        for i in range(len(prices)):
            min_price=min(min_price,prices[i])
            max_price=max(max_price,prices[i]-min_price)
        return max_price