class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=0
        neg=1
        n=len(nums)
        a=[0]*n
        for i in range(n):
            if nums[i]>0:
                a[pos]=nums[i]
                pos+=2
            else:
                a[neg]=nums[i]
                neg+=2
        return a