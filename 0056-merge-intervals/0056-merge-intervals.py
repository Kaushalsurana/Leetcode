class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        k=[]
        for i in range(len(intervals)):
            if not k or intervals[i][0]>k[-1][1]:
                k.append(intervals[i])
            else:
                k[-1][1]=max(k[-1][1],intervals[i][1])
        return k