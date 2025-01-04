from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum1=0
        d=defaultdict(int)
        d[0]=1
        count=0
        for i in range(len(nums)):
            sum1+=nums[i]
            diff=sum1-k
            count+=d[diff]
            d[sum1]+=1
        return count