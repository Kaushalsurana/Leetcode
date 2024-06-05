class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l=len(words)
        a=[]
        for i in words[0]:
            k=True
            for j in range(1,l):
                if i in words[j] and k:
                    words[j]=words[j].replace(i,"",1)
                    k=i
                else:
                    k=None
            if k==i:
                a.append(i)
        return a