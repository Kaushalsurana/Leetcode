class Solution:
    def findComplement(self, num: int) -> int:
        a=bin(num)[2:]
        b=""
        for i in a:
            if i=='0':
                b+="1"
            else:
                b+="0"
        return int(b,2)
