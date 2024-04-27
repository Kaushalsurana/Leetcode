class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def dfs(i_r, i_k):
            if i_k == len(key):
                return 0
            cost = inf
            for i in r[key[i_k]]:
                steps = abs(i - i_r)
                cost = min(min(steps, len(ring)-steps) + dfs(i, i_k+1) + 1, cost)
            return cost

        r = defaultdict(list)
        for i, ch in enumerate(ring):
            r[ch].append(i)
        return dfs(0, 0)