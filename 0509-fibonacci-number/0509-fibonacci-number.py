class Solution:
    def fib(self, n: int) -> int:
        second=0
        last=1
        output=0
        if n==1:
            return 0
        elif n==0:
            return 0
        for i in range(n-1):
            output=second+last
            second=last
            last=output
        return last