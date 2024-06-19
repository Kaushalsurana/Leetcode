class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def bouq(mid):
            flower=0
            bou=0
            for i in bloomDay:
                if i<=mid:
                    flower+=1
                    if flower==k:
                        bou+=1
                        flower=0
                else:
                    flower=0
                if bou>=m:
                    return True
            return bou>=m

        if m*k>len(bloomDay):
            return -1
        low,high=min(bloomDay),max(bloomDay)
        while low<high:
            mid=(low+high)//2
            if bouq(mid):
                high=mid
            else:
                low=mid+1
        return low

        