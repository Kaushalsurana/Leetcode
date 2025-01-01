class Solution:
    def rob(self, nums: List[int]) -> int:
        def ge(nums):
            maxi,prev=0,0
            for i in nums:
                curr=max(maxi,prev+i)
                prev=maxi
                maxi=curr
            return maxi
        if len(nums)==1:
            return nums[0]
        return max(ge(nums[:-1]),ge(nums[1:]))