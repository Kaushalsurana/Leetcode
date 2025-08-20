class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=set()
        l=0
        cur=0
        for i in range(len(s)):
            while s[i] in m:
                m.remove(s[l])
                l+=1
            m.add(s[i])
            cur=max(cur,i-l+1)
        return cur