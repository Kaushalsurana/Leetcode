class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        a=0
        for i in range(n):
            ls=ll=rs=rl=0
            for j in range(i):
                if rating[j]<rating[i]:
                    ls+=1
                if rating[j]>rating[i]:
                    ll+=1
            for k in range(i+1,n):
                if rating[k]>rating[i]:
                    rl+=1
                if rating[k]<rating[i]:
                    rs+=1
            a+=ls*rl+ll*rs
        return a
                