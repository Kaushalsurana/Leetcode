class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        x = 1
        while x in nums:
            x+=1
        return x