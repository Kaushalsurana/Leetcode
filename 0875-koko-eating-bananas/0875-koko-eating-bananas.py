class Solution:
    def m(self,p,n):
        t=0
        for i in p:
            t+=math.ceil(i/n)
        return t
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high=max(piles)
        low=1
        while low<=high:
            mid=(low+high)//2
            res=self.m(piles,mid)
            if res<=h:
                high=mid-1
            else:
                low=mid+1        
        return low