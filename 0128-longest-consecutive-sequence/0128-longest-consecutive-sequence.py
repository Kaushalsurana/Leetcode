class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        count=0
        res=0
        for i in a:
            if i-1 not in a:
                b=i
                count=1
                while b+1 in a:
                    b+=1
                    count+=1
                res=max(res,count)
        return res
        