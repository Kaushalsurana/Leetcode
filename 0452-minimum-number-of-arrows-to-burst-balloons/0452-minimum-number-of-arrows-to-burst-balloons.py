class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        a=sorted(points,key=lambda x:x[1])
        b=None
        count=0
        for p in a:
            if b is None or b<p[0]:
                count+=1
                b=p[1]
        return count