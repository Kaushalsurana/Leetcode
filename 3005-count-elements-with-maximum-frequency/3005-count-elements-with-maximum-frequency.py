class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=defaultdict(int)
        m,c=0,0
        for i in nums:
            d[i]+=1
            if d[i]>m:
                m=d[i]
                c=0
            if d[i]==m:
                c+=1
        return m*c