class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a=set()
        n=len(nums)
        for i in range(n):
            j=i+1
            k=n-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==0:
                    a.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif s<0:
                    j+=1
                else:
                    k-=1
        return list(a)