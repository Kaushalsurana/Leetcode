class Solution:
    def romanToInt(self, s: str) -> int:
        s=s.replace("IV", "IIII")
        s=s.replace("IX", "VIIII")
        s=s.replace("XL", "XXXX")
        s=s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s=s.replace("CM","DCCCC")
        num=0
        for i in s:
            if i=="I":
                num+=1
            elif i=="V":
                num+=5
            elif i=="X":
                num+=10
            elif i=="L":
                num+=50
            elif i=="C":
                num+=100
            elif i=="D":
                num+=500
            else:
                num+=1000
        return num

