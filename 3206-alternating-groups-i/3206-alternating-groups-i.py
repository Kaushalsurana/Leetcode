class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        a=0
        k=len(colors)
        for i in range(k):
            b=colors[i]
            c=colors[(i+1)%k]
            d=colors[(i+2)%k]
            if b!=c and c!=d and b==d:
                a+=1
        return a