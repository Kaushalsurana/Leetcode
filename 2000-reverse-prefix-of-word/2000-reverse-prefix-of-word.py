class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        k=''
        n=len(word)
        for i in range(n):
            if word[i]==ch:
                k=word[i::-1]
                break
        return k+word[len(k):]
