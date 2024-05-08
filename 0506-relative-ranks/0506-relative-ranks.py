class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=sorted(score,reverse=True)
        r={}
        for i,p in enumerate(s):
            if i==0:
                r[p]="Gold Medal"
            elif i==1:
                r[p]="Silver Medal"
            elif i==2:
                r[p]="Bronze Medal"
            else:
                r[p]=str(i+1)
        final=[]
        for i in range(len(score)):
            final.append(r[score[i]])
        return final