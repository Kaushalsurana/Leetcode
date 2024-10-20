class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i+1]>nums[i]:
                a=i
                break
        if a==-1:
            return nums.reverse()
        for i in range(n-1,a,-1):
            if nums[i]>nums[a]:
                nums[a],nums[i]=nums[i],nums[a]
                break
        
        nums[a+1:]=reversed(nums[a+1:])
        return nums