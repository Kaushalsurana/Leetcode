class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        k=0
        z=arrays[0][-1]
        y=arrays[0][0]
        for i in arrays[1:]:
            m=i[0]
            n=i[-1]
            k=max(n-y,z-m,k)
            y=min(y,m)
            z=max(z,n)
        return k
