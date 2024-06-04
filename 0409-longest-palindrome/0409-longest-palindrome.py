class Solution:
    def longestPalindrome(self, s: str) -> int:
        a=set()
        for i in s:
            if i in a:
                a.remove(i)
            else:
                a.add(i)

        if len(a)==0:
            return len(s)
        else:
            return len(s)-len(t)