class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a=list(range(1,n+1))
        b=0
        while n>1:
            b=(b+(k-1))%n
            a.pop(b)
            n-=1
        return a[0]