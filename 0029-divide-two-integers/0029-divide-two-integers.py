class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign= (dividend<0)^(divisor<0)
        q=0
        n=abs(dividend)
        a=abs(divisor)
        while n>=a:
            w=0
            while n >= (a << (w + 1)):
                w += 1
            q+=1<<w
            n-=a<<w
        res = -q if sign else q
        return min(max(-2**31, res), 2**31 - 1)