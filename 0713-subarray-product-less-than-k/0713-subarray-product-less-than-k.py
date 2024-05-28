class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left=0
        count=0
        product=1
        for right in range(len(nums)):
            product *=nums[right]
            while k<=product and left<=right:
                product /= nums[left]
                left+=1
            count +=right-left+1
        return count