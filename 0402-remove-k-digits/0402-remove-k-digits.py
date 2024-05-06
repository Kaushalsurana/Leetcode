class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans=[]
        for i in num:
            while k>0 and ans and ans[-1]>i:
                ans.pop()
                k-=1
            ans.append(i)
        while k>0:
            ans.pop()
            k-=1    
        
        res="".join(ans).lstrip("0")
        return res if res else "0"  