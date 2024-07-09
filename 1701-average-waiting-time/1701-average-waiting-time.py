class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current = 0
        n = len(customers)
        leaving = [0] * n
        
        for i in range(n):
            arrival, time = customers[i]
            current = max(current, arrival)
            current += time
            leaving[i] = current
        
        total = sum(leaving[i] - customers[i][0] for i in range(n))
        average = total / n
        
        return average