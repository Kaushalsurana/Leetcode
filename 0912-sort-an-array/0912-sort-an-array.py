class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        a=[]
        k=[]
        for num in nums:
            heapq.heappush(a,num)

        for i in range(len(a)):
            k.append(heapq.heappop(a))
        return k