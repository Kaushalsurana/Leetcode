class Solution:
    def minimumDeletions(self, s: str) -> int:
        a=b=0
        for i in s:
            if i=='b':
                a+=1
            elif a:
                b+=1
                a-=1
        return b