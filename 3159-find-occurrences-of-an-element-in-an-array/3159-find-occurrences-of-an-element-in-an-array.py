class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        o=[]
        for i,n in enumerate(nums):
            if n==x:
                o.append(i)
        ans=[]
        for k in queries:
            if k<=len(o):
                ans.append(o[k-1])
            else:
                ans.append(-1)
        return ans