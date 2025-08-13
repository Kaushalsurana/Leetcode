class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                le=s[l+1:r+1]
                ri=s[l:r]
                return le==le[::-1] or ri==ri[::-1]
            l+=1
            r-=1
        return True