class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma=-sys.maxsize-1
        sum=0
        for i in nums:
            sum+=i
            if sum>ma:
                ma=sum
            if sum<0:
                sum=0
        return ma