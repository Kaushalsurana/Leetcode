class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=Counter(nums)
        n=len(nums)
        for i,j in c.items():
            if j>=n/2:
                return i