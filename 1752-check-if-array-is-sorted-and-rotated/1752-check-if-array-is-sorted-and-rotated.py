class Solution:
    def check(self, nums: List[int]) -> bool:
        count=0
        for i in range(1,len(nums)):
            if(nums[i-1]>nums[i]):
                count+=1
        n=len(nums)
        if (nums[n-1]>nums[0]):
            count+=1
        if count==0 or count==1:
            return True
        else:
            return False