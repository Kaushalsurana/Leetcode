class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        a=[]
        for i in range(len(worker)):
            a.append((difficulty[i],profit[i]))
        a.sort()
        worker.sort()
        k,b,c=0,0,0
        for i in worker:
            while b<len(a) and i>=a[b][0]:
                c=max(c,a[b][1])
                b+=1
            k+=c
        return k