class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        if len(s)==0:
            return True
        for i in s:
            if i == '(' or i == '{' or i == '[':
                a.append(i)
            else:
                if len(a) == 0:
                    return False
                b = a[-1]
                a.pop()
                if (i == ')' and b == '(') or (i == ']' and b == '[') or (i == '}' and b == '{'):
                    continue
                else:
                    return False
        return len(a) == 0