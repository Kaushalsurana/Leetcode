class Solution:
    def reverseParentheses(self, s: str) -> str:
        a=[]
        for i in s:
            if i==')':
                k=""
                while a[-1] !='(':
                    k+=a.pop()
                a.pop()
                for j in k:
                    a.append(j)
            else:
                a.append(i)
        return "".join(a)