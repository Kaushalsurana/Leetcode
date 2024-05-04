class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)

        res = 0
        for row in matrix:
            for col_idx in range(cols):
                heights[col_idx] = heights[col_idx] + 1 if row[col_idx] == '1' else 0
            
            stack = []
            for j in range(len(heights)):
                while stack and heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j if not stack else j - stack[-1] - 1

                    res = max(res, h * w)
                
                stack.append(j)

        return res