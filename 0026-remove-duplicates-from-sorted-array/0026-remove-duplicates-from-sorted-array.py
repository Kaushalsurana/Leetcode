class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 
        a,b=0,1
        while b<len(nums):
            if nums[a]==nums[b]:
                b+=1
            else:
                a+=1
                nums[a]=nums[b]
                b+=1
        return a+1