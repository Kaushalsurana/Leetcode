class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0]*26
        n=len(s)
        dp[ord(s[0])-ord('a')]=1
        for i in range(1,n):
            a=ord(s[i])-ord('a')
            lo=max(0,a-k)
            up=min(26,a+k+1)
            max_value=0
            for j in range(lo,up):
                max_value = max(max_value, dp[j])
            dp[a]=1+max_value
        return max(dp)