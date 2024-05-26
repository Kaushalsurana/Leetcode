class Solution:
    def compressedString(self, word: str) -> str:
        a=""
        while word:
            b=word[0]
            l=1
            while l<9 and l<len(word) and word[l]==b:
                l+=1
            a+=str(l)+b
            word=word[l:]
        return a