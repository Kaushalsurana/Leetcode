class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp=[[-1] * n for _ in range(k+1)]
        def s(i:int,j:int) -> int:
            if i ==k:
                return 0
            if dp[i][j] !=-1:
                return dp[i][j]
            po=stayScore[i][j]+s(i+1,j)
            for l in range(n):
                if l!=j:
                    po=max(po,travelScore[j][l]+s(i+1,l))
            dp[i][j]=po
            return po
        return max(s(0,o) for o in range(n))