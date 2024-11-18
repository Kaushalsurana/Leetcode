class Solution:
    def myAtoi(self, s: str) -> int:
        k=0
        for i in s:
            if i==" ":
                k+=1
            else:
                break
        sign = 1
        n=len(s)
        if k < n and s[k] == '-':
            sign = -1
            k += 1
        elif k < n and s[k] == '+':
            k += 1
        res=0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        while k<n and s[k].isdigit():
            y=int(s[k])
            if res>(INT_MAX -y)//10:
                return INT_MAX if sign==1 else INT_MIN
            res=res*10+y
            k+=1
        return sign*res
        

                