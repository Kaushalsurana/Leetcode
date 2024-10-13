from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n=len(nums)
        res=[]
        for i in range(n-k+1):
            arr=nums[i:i+k]
            c=Counter(arr)
            p=sorted(c.items(),key=lambda a: (-a[1],-a[0]))
            total=0
            for a,b in p[:x]:
                total+=a*b
            res.append(total)
        return res
        