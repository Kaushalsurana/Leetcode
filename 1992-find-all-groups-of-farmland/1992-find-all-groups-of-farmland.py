class Solution:
    def findFarmland(self, land_map):
        def explore(row_idx, col_idx):
            if row_idx < 0 or row_idx >= rows or col_idx < 0 or col_idx >= cols or land_map[row_idx][col_idx] != 1:
                return
            
            land_map[row_idx][col_idx] = 2
            
            nonlocal top_left_corner, bottom_right_corner
            top_left_corner = [min(top_left_corner[0], row_idx), min(top_left_corner[1], col_idx)]
            bottom_right_corner = [max(bottom_right_corner[0], row_idx), max(bottom_right_corner[1], col_idx)]
            
            explore(row_idx + 1, col_idx)
            explore(row_idx - 1, col_idx)
            explore(row_idx, col_idx + 1)
            explore(row_idx, col_idx - 1)
        
        rows, cols = len(land_map), len(land_map[0])
        farming_areas = []
        
        for i in range(rows):
            for j in range(cols):
                if land_map[i][j] == 1:
                    top_left_corner = [i, j]
                    bottom_right_corner = [i, j]
                    explore(i, j)
                    farming_areas.append([top_left_corner[0], top_left_corner[1], bottom_right_corner[0], bottom_right_corner[1]])
        
        return farming_areas
