class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x=0
        for i in nums:
            x=x^i
        c=0
        while k or x:
            if (k%2)!=(x%2):
                c+=1
            k//=2
            x//=2
        return c