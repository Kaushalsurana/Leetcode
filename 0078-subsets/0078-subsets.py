class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for i in nums:
            p=len(res)
            for j in range(p):
                s=list(res[j])
                s.append(i)
                res.append(s)
        return res