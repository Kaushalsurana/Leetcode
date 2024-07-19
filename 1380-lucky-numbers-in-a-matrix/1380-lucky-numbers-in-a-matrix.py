class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        a=[]
        b=[]
        c=[]
        for i in range(len(matrix)):
            a.append(min(matrix[i]))
        for i in range(len(matrix[0])):
            k=-1
            for j in range(len(matrix)):
                if k<matrix[j][i]:
                    k=matrix[j][i]
            b.append(k)
        for i in range(len(a)):
            if a[i] in b:
                c.append(a[i])
        return c