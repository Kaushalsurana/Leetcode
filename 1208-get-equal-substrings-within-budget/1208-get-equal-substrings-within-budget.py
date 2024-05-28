class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        a=0
        b=0
        c=0
        for r in range(len(s)):
            b+=abs(ord(s[r])-ord(t[r]))
            while (b>maxCost):
                b-=abs(ord(s[r])-ord(t[r]))
                c+=1
            a=max(a,r-c+1)
        return a