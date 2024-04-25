class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        result=1
        count=1
        for i in range(0,len(s)-1):
            if ord(s[i])+1==ord(s[i+1]):
                count+=1
            else:
                result=max(count,result)
                count=1
        result=max(count,result)
        return result