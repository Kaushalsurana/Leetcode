class Solution:
    def tribonacci(self, n: int) -> int:
        if n<2:
            return n
        if n==2:
            return 1
        a0,a1,a2=0,1,1
        new=0
        for i in range(2,n):
            new=a0+a1+a2
            a0,a1,a2=a1,a2,new
        return new