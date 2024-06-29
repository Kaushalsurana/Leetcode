class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        a=[0]*n
        b=0
        for i,j in roads:
            a[i]+=1
            a[j]+=1
        a.sort()
        for i in range(len(a)):
            b+=a[i]*(i+1)
        return b