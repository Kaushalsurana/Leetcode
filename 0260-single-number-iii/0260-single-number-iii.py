class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=Counter(nums)
        b=[]
        for i,j in a.items():
            if j==1:
                b.append(i)
        return b