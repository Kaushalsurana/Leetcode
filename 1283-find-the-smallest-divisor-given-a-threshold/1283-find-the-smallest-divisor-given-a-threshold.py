class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low,high=1,max(nums)
        while low<=high:
            mid=(low+high)//2
            k=sum(math.ceil(i/mid) for i in nums)
            # for i in nums:
            #     k+=math.ceil(i/mid)
            if k<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low
            