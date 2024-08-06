class Solution:
    def minimumPushes(self, word: str) -> int:
        c=[0]*26
        for i in word:
            c[ord(i)-ord('a')]+=1
        c=sorted(c,reverse=True)
        ans = sum(c[:8]) * 1
        ans += sum(c[8:16]) * 2
        ans += sum(c[16:24]) * 3
        ans += sum(c[24:]) * 4
        return ans