class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        a=1
        b=0
        c=0
        while a<=n:
            if b<len(nums) and nums[b]<=a:
                a+=nums[b]
                b+=1
            else:
                a+=a
                c+=1
        return c
                