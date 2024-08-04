class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub=[]
        res=0
        for i in range(len(nums)):
            sum=0
            for j in range(i,len(nums)):
                sum+=nums[j]
                sub.append(sum)
        sub.sort()
        mod=10**9+7
        for i in range(left-1,right):
            res=(res+sub[i])%mod
        return res
