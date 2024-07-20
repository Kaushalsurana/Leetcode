class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        a,b=len(rowSum),len(colSum)
        m=[[0]*b for _ in range(a)]
        for i in range(a):
            for j in range(b):
                m[i][j]=min(rowSum[i],colSum[j])
                rowSum[i]-=m[i][j]
                colSum[j]-=m[i][j]
        return m