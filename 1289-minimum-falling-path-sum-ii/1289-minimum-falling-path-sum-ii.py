class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        a=len(grid)
        for i in range(1,a):
            k=sorted(grid[i-1])
            for j in range(a):
                if grid[i-1][j]==k[0]:
                    grid[i][j]+=k[1]
                else:
                    grid[i][j]+=k[0]
        return min(grid[a-1])
