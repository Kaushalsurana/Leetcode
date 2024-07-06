class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        a=0
        while time>0:
            while time>0 and a<n-1:
                a+=1
                time-=1
            while time>0 and a>0:
                a-=1
                time-=1
        return a+1