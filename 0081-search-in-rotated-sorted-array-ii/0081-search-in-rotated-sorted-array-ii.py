class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        high=len(nums)-1
        low=0
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            elif nums[high]>=nums[mid]:
                if nums[mid]<=target and nums[high]>=target:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[low]<=target and nums[mid]>=target:
                    high=mid-1
                else:
                    low=mid+1
        return False