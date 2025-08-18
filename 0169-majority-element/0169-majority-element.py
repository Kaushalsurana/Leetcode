class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a={}
        n=len(nums)//2
        if n==0:
            return nums[0]
        for i in nums:
            if i in a:
                a[i]+=1
                if a[i]>n:
                    return i
            else:
                a[i]=1