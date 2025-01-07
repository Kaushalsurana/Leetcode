class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def au(bloomDay,day,m,k):
            a=0
            res=0
            for i in bloomDay:
                if day>=i:
                    a+=1
                else:
                    res+=a//k
                    a=0
            res+=a//k
            return res>=m
        if m*k>len(bloomDay):
            return -1
        mi=min(bloomDay)
        ma=max(bloomDay)
        while mi<=ma:
            mid=(mi+ma)//2
            if au(bloomDay,mid,m,k):
                ma=mid-1
            else:
                mi=mid+1
        return mi