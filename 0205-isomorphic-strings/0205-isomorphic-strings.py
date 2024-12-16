class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            a1=s[i]
            a2=t[i]
            if a1 in a and a[a1]!=a2:
                return False
            a[a1]=a2
        return True