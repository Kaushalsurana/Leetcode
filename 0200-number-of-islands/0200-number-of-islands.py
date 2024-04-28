class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        no=0

        def check(k,l):
            if k<0 or k==m or l<0 or l==n or grid[k][l]=='0':
                return 

            grid[k][l]='0'
            check(k-1,l)
            check(k+1,l)
            check(k,l+1)
            check(k,l-1)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    check(i,j)
                    no+=1
        return no