from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=Counter(nums)
        nums[:]=[0]*s[0]+[1]*s[1]+[2]*s[2]
        return nums