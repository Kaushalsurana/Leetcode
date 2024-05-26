class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=[num for num,c in count.items() if c==2]
        if len(res)==0:
            return 0
        a=0
        for i in res:
            a=a^i
        return a