class Solution:
    def possibleStringCount(self, word: str) -> int:
        n=len(word)
        c=1
        for i in range(1,n):
            if word[i]==word[i-1]:
                c+=1
        return c