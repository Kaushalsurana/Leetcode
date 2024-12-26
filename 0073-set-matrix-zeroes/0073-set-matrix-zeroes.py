class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a=matrix
        k=[]
        l=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    k.append(i)
                    l.append(j)

        for row in k:
            for col in range(len(matrix[0])):
                a[row][col] = 0

        for col in l:
            for row in range(len(matrix)):
                a[row][col] = 0
        return a