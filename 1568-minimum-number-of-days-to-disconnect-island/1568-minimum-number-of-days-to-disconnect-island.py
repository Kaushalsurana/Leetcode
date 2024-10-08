class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        def dfs(row,col,visited):
            if row<0 or row>=ROWS or col<0 or col>=COLS or (row,col) in visited or grid[row][col]==0: return 
            visited.add((row,col))
            for new_row,new_col in ((row,col+1),(row+1,col),(row-1,col),(row,col-1)):
                dfs(new_row,new_col,visited)
        def island_count():
            islands = 0
            visited = set()
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1 and (r,c) not in visited:
                        dfs(r,c,visited)
                        islands += 1
            return islands
        if island_count() != 1: return 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 : continue
                grid[r][c] = 0
                if island_count() != 1 : return 1
                grid[r][c] = 1
        return 2