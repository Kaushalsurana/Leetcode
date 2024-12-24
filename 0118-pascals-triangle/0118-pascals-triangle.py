class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        if numRows>=1:
            l.append([1])
        if numRows>=2:
            l.append([1,1])
        for i in range(2,numRows):
            k=[0]*(i+1)
            k[0],k[-1]=1,1
            for j in range(1,i):
                k[j]=l[i-1][j-1]+l[i-1][j]
            l.append(k)
        return l
