class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        t=0
        current=maximumHeight[0]
        for k in maximumHeight:
            if current<=0:
                return -1
            a=min(current,k)
            t+=a
            current=a-1
        return t