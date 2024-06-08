class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2:
            return False
        a=0
        b={0:-1}
        for i in range(len(nums)):
            a+=nums[i]
            mod=a%k
            if mod in b:
                if i-b[mod]>1:
                    return True
            else:
                b[mod]=i
        return False