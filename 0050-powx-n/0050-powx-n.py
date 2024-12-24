class Solution:
    def myPow(self, x: float, n: int) -> float:
        a=n
        ans=1.0
        if a<0:
            a*=-1
        while a:
            if a%2==1:
                ans*=x
                a-=1
            else:
                x*=x
                a=a//2
        if n<0:
            return 1.0/ans
        return ans