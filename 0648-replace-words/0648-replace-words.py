class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        a=sentence.split(" ")
        for i in dictionary:
            for j,k in enumerate(a):
                if k.startswith(i):
                    a[j]=i
        return " ".join(a)