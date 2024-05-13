class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = sorted((wage[i] / quality[i], quality[i]) for i in range(n))
        min_cost = float('inf')
        sum_quality = 0
        max_heap = []

        for ratio, qual in workers:
            heapq.heappush(max_heap, -qual)
            sum_quality += qual

            if len(max_heap) > k:
                sum_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                min_cost = min(min_cost, sum_quality * ratio)

        return min_cost