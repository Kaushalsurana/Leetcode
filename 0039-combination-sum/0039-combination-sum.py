class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def gen(a,arr,tar):
            if sum(arr)==target:
                res.append(arr[:])
                return
            if sum(arr)>target:
                return
            for i in range(a,len(candidates)):
                arr.append(candidates[i])
                gen(i,arr,tar)
                arr.pop()
        res=[]
        gen(0,[],target)
        return res