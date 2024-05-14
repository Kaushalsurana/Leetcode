class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        def ge(i,j,sum):
            if i<0 or i>=r or j<0 or j>=c or grid[i][j]==0:
                return sum
            t=grid[i][j]
            sum+=t
            grid[i][j]=0
            a=max(ge(i+1,j,sum),ge(i-1,j,sum),ge(i,j+1,sum),ge(i,j-1,sum))
            grid[i][j]=t
            return a
        g=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]!=0:
                    g=max(ge(i,j,0),g)
        return g