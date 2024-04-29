class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        k=len(grid)
        l=len(grid[0])
        side=0
        for i in range(k):
            for j in range(l):
                if grid[i][j]==1:
                    side+=4
                    if i<k-1 and grid[i+1][j]==1:
                        side-=2
                    if j<l-1 and grid[i][j+1]==1:
                        side-=2
        return side