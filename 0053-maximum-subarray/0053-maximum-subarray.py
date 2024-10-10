class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        m = -sys.maxsize-1
        for i in nums:
            sum+=i
            if sum>m:
                m=sum
            if sum<0:
                sum=0
        return m
            