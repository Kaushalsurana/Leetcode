class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            k=i%3
            if k==1:
                a+=1
            elif k==2:
                a+=1
        return a