class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        ans[0]=self.search(nums,target,0)
        ans[1]=self.search(nums,target,1)
        return ans
    def search(self,nums,target,y):
        n=len(nums)
        high=n-1
        low=0
        i=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                i=mid
                if y==0:
                    high=mid-1
                else:
                    low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return i