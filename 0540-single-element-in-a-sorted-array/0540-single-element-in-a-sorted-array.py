class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        low,high=1,n-2
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        while low<=high:
            mid=(low+high)//2
            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]
            if nums[mid]==nums[mid+1]:
                if mid%2:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if mid%2:
                    low=mid+1
                else:
                    high=mid-1
                    