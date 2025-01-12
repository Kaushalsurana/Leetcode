class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                s=[]
                for k in range(j+1,n):
                    u=nums[i]+nums[j]+nums[k]
                    four=target-u
                    if four in s:
                        p=[nums[i], nums[j], nums[k], four]
                        p.sort()
                        a.add(tuple(p))
                    s.append(nums[k])
        return list(a)
