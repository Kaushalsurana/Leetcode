import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        high=len(nums)-1
        low=0
        least=math.inf
        while low<=high:
            mid=(high+low)//2
            if nums[low]<=nums[mid]:
                least=min(least,nums[low])
                low=mid+1
            else:
                least=min(least,nums[mid])
                high=mid-1
        return least