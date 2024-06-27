class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a=edges[0][0]
        b=edges[0][1]
        return a if a==edges[1][0] or a==edges[1][1] else b