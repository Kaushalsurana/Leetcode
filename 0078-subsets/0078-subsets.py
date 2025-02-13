
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def gen(a,arr):
            res.append(arr[:])
            for i in range(a,len(nums)):
                arr.append(nums[i])
                gen(i+1,arr)
                arr.pop()
        gen(0,[])
        return res