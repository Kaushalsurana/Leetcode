class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        high,low=len(arr),0
        while low<high:
            mid=(low+high)//2
            if arr[mid]-mid>k:
                high=mid
            else:
                low=mid+1
        return low+k