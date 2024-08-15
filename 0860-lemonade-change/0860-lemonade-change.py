class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a=0
        b=0
        for i in bills:
            if i==5:
                a+=1
            elif i==10:
                if a>0:
                    a-=1
                    b+=1
                else:
                    return False
            else:
                if a>0 and b>0:
                    a-=1
                    b-=1
                elif a>=3:
                    a-=3
                else:
                    return False
        return True
            
