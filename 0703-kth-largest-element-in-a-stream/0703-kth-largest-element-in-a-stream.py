class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=[]
        self.k=k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        heappush(self.nums,val)
        if len(self.nums)>self.k:
            heappop(self.nums)
        return self.nums


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)