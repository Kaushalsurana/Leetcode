class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        sum=0
        for i in range(k):
            happiness[i]=max(happiness[i]-i,0)
            sum+=happiness[i]
        return sum 
