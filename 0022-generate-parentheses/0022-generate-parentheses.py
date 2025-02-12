class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(n,open,close,st,res):
            if open==close==n:
                res.append(st)
                return
            if open<n:
                gen(n,open+1,close,st+"(",res)
            if close<open:
                gen(n,open,close+1,st+")",res)
        res=[]
        gen(n,0,0,"",res)
        return res