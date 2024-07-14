class Solution:
    def countOfAtoms(self, formula: str) -> str:
        dic = collections.defaultdict(int)
        cnt = 0
        co_eff = 1
        i,ele = 0,""
        stack = []
        for c in formula[::-1]:
            if c.isdigit():
                cnt += int(c)*(10**i)
                i += 1
            elif c == ')':
                if cnt>0:
                    stack.append(cnt)
                    co_eff = co_eff*cnt
                i,cnt=0,0
            elif  c== "(":
                if stack:
                    co_eff = co_eff//stack.pop()
                i,cnt = 0,0
            elif c.islower():
                ele = c + ele
            elif c.isupper():
                ele = c + ele
                dic[ele] += (cnt or 1)*co_eff
                ele = ""
                i,cnt=0,0
        return "".join(k + str(v > 1 and v or "") for k, v in sorted(dic.items()))