class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def gen(a,arr,tar):
            if tar==0:
                res.append(arr[:])
                return
            if tar<0:
                return
            for i in range(a,len(candidates)):
                if candidates[i]>target:
                    break
                if i>a and candidates[i]==candidates[i-1]:
                    continue
                arr.append(candidates[i])
                gen(i+1,arr,tar-candidates[i])
                arr.pop()
        res=[]
        candidates.sort()
        gen(0,[],target)
        return res