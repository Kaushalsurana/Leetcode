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

        high,low=sum(weights),max(weights)
        while low<=high:
            mid=(low+high)//2
            da=k(weights,mid)
            if da<=days:
                high=mid-1
            else:
                low=mid+1
        return low