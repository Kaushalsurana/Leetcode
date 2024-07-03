class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n=len(nums)
        if n<4:
            return 0
        nums.sort()
        k=math.inf
        for i in range(4):
            k=min(k,nums[n-4+i]-nums[i])
        return k