class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color={}
        coun={}
        res=[]
        for x,y in queries:
            c=color.get(x)
            if c is not None:
                coun[c]-=1
                if coun[c]==0:
                    del coun[c]
            color[x]=y
            if y in coun:
                coun[y]+=1
            else:
                coun[y]=1
            res.append(len(coun))
        return res