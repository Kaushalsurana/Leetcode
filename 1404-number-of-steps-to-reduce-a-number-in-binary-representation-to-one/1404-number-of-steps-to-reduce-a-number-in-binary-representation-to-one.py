class Solution:
    def numSteps(self, s: str) -> int:
        a=int(s,2)
        b=0
        while a>1:
            b+=1
            if a%2==0:
                a//=2
            else:
                a+=1
        return b
        