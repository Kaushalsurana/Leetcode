class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a=[]
        b=0
        for i in s:
            if i==")":
                b-=1
            if b>0:
                a.append(i)
            if i=="(":
                b+=1
        return ''.join(a)