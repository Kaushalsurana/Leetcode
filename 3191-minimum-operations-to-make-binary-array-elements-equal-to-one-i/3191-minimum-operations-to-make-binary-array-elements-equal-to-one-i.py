class Solution:
    def minOperations(self, nums: List[int]) -> int:
        k=0
        i=0
        while i<=len(nums)-3:
            if nums[i]==0:
                nums[i]=1-nums[i]
                nums[i+1]=1-nums[i+1]
                nums[i+2]=1-nums[i+2]
                k+=1
            i+=1
        for i in nums:
            if i==0:
                return -1
        return k