class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        mn, mx, l = 1, max(position)-min(position), 0
        n = len(position)
        position.sort()
        def df(dist):
            c, prev = 1, position[0]
            for i in range(1,len(position)):
                if position[i]-prev>=dist: 
                    prev = position[i]
                    c += 1
            return c>=m
        while mn<=mx:
            mid=(mn+mx)>>1
            if df(mid): 
                l = mid
                mn = mid + 1
            else: 
                mx = mid-1
        return l