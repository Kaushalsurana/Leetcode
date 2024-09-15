class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m=len(grid)
        n=len(grid[0])
        k={}
        if grid[m-1][n-1]==1:
            health-=1
        def check(x,y,health):
            if x < 0 or x >= m or y < 0 or y >= n or health <= 0:
                return False
            if x == m - 1 and y == n - 1:
                return health > 0
            if (x, y, health) in k:
                return k[(x, y, health)]
            k[(x,y,health)]=False
            
            new=health-grid[x][y]
            if (check(x + 1, y, new) or check(x - 1, y, new) or  check(x, y + 1, new) or  check(x, y - 1, new)): 
                k[(x, y, health)] = True
            return k[(x,y,health)]
        return check(0,0,health)