from graphlib import CycleError, TopologicalSorter

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def toposort(edges):
            pred = {x: [] for x in range(1, k + 1)}  # predecessors
            for x, y in edges:
                pred[y].append(x)
            ts = TopologicalSorter(pred)
            try:
                return list(ts.static_order())
            except CycleError:
                return []

        rowOrder = toposort(rowConditions)
        colOrder = toposort(colConditions)
        if not rowOrder or not colOrder:
            return []

        rowPos = {x: i for i, x in enumerate(rowOrder)}
        colPos = {x: i for i, x in enumerate(colOrder)}
        ans = [[0] * k for _ in range(k)]
        for x in range(1, k + 1):
            ans[rowPos[x]][colPos[x]] = x
        return ans