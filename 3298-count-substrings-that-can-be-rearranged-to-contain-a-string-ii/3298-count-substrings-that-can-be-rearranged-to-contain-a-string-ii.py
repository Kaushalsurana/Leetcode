class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        c1=defaultdict(int)
        c2=defaultdict(int)
        a,b=len(word1),len(word2)
        if b>a:
            return 0
        for c in word2:
            c2[c]+=1
        res=0
        required=len(c2)
        le=0
        fo=0
        for i in range(a):
            c=word1[i]
            c1[c]+=1
            if c in c2 and c1[c]==c2[c]:
                fo+=1
            while fo==required:
                res+=(a-i)
                q=word1[le]
                c1[q]-=1
                if q in c2 and c1[q]<c2[q]:
                    fo-=1
                le+=1
        return res