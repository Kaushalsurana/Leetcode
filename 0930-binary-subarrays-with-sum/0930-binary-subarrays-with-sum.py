class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        i, j, sum_val, count, freq = 0, 0, 0, 0, 0

        while i < len(nums):
            sum_val += nums[i]
            if nums[i] == 1:
                freq = 0
            if sum_val > goal:
                sum_val -= nums[j]
                j += 1
            while j <= i and sum_val == goal:
                sum_val -= nums[j]
                j += 1
                freq += 1
            count += freq
            i += 1
        return count