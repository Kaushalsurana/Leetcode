class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=0
        i,j=0,1
        while j<len(prices):
            if prices[i]<prices[j]:
                y=prices[j]-prices[i]
                a=max(a,y)
            else:
                i=j
            j+=1
        return a