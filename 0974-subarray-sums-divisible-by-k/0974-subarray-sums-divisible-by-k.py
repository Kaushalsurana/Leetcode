class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        a=[0]*k
        a[0]=1
        b=0
        c=0
        n=len(nums)
        for i in range(n):
            b+=nums[i]
            d=b%k
            if d<0:
                d+=k
            c+=a[d]
            a[d]+=1
        return c