class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        n=len(nums)
        for i in range(n):
            k=nums[i]
            rem=target-k
            if rem in d:
                return(d[rem],i)
            d[k]=i
        return[-1,-1]