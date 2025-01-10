class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # if nums[0]==nums[1]:
        #     return nums[0]
        for i in range(len(nums)):
            k=abs(nums[i])
            if nums[k]<0:
                return k
            nums[k]=-nums[k]
        