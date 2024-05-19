class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        n=len(nums)
        count=0
        min_diff=float('inf')
        for i,j in enumerate(nums):
            if j^k>j:
                nums[i]^=k
                count+=1
            min_diff=min(min_diff,nums[i]-(nums[i]^k))
        return sum(nums)-(min_diff if count&1 else 0)