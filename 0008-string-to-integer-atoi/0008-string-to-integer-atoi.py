class Solution:
    def myAtoi(self, s: str) -> int:
        sign=1
        a=0
        for i in s:
            if i!=" ":
                break
            a+=1
        n=len(s)
        if a<n:
            if s[a]=='-':
                sign=-1
                a+=1
            elif s[a]=='+':
                sign=1
                a+=1
        res=0
        INT_MAX=2**31-1
        INT_MIN=-2**31
        while a<n and s[a].isdigit():
            b=int(s[a])
            if res>(INT_MAX-b)//10:
                return INT_MAX if sign==1 else INT_MIN
            res=res*10+b
            a+=1
        return sign*res
        
        

                