from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=Counter(nums)
        n=len(nums)
        res=[]
        for i,j in a.items():
            if j>(n/3):
                res.append(i)
        return res