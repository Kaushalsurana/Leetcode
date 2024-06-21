class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        if minutes>=n:
            return sum(customers)

        sun,a,b=0,0,0
        for i in range(n):
            if grumpy[i]==0:
                sun+=customers[i]
            else:
                a+=customers[i]
            if i-minutes>=0 and grumpy[i-minutes]==1:
                a-=customers[i-minutes]
            if a>b:
                b=a
        return sun+b