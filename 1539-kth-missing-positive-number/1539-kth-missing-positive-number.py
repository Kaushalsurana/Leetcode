class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        a=[]
        count=0
        for i in range(1,arr[-1]+1):
            if i not in arr:
                a.append(i)
                count+=1
            if count==k:
                return a[-1]
        return arr[-1]+k-count