class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        k=len(nums)
        for i in nums:
            if i<0 and -i in nums:
                return -i
        return -1