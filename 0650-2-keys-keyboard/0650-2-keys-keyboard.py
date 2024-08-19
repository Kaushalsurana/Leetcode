class Solution:
    def minSteps(self, n: int) -> int:
        a=1
        b=0
        count=0
        while a!=n:
            if n%a==0:
                b=a
                count+=1
            
            count+=1
            a+=b
        return count