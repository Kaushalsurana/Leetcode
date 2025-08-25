class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        c={}
        l=0
        ma=0
        for r in range(len(s)):
            c[s[r]]=1+c.get(s[r],0)
            ma=max(ma,c[s[r]])
            while (r-l+1)-ma>k:
                c[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res