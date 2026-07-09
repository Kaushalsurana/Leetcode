class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        f=matrix
        a=set()
        b=set()
        for i in range(len(f)):
            for j in range(len(f[0])):
                if f[i][j]==0:
                    a.add(i)
                    b.add(j)
        for i in a:
            for j in range(len(f[i])):
                matrix[i][j]=0
        for i in b:
            for j in range(len(f)):
                matrix[j][i]=0
        return matrix
