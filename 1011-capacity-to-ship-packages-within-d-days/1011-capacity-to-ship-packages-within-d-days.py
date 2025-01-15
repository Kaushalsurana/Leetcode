class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def k(we,m):
            day=1
            y=0
            for i in range(len(we)):
                if y+we[i]>m:
                    day+=1
                    y=we[i]
                else:
                    y+=we[i]
            return day
        q=sum(weights)
        high,low=q,max(weights)
        while low<=high:
            mid=(low+high)//2
            if q/mid>days:
                low=mid+1
                continue
            da=k(weights,mid)
            if da<=days:
                high=mid-1
            else:
                low=mid+1
        return low