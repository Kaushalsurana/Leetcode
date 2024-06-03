class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        a=0
        for i in range(len(s)):
            if s[i]==t[a]:
                if a==len(t)-1:
                    a+=1
                    break
                a+=1
        size=len(t)-a
        return size