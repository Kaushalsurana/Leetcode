class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a=target-nums[i]
            nums.pop(i)
            print(nums)
            if a in nums:
                b=nums.index(a)
                return [i,b+i+1]
        

