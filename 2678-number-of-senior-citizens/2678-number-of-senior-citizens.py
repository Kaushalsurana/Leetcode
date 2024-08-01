class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in details:
            a=int(i[11:13])
            print(a)
            if a>60:
                c+=1
        return c