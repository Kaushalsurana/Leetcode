class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        a=0
        for i in range(len(nums)-1):
            if nums[i+1]<=nums[i]:
               b= nums[i]-nums[i+1] +1
               nums[i+1]+=b
               a+=b
        return a