class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ans = float("inf")
        total_ones = sum(nums)
        cur_ones = sum(nums[-total_ones:])
        for i in range(len(nums)):
            cur_ones += (nums[i] == 1) - (nums[i - total_ones] == 1)
            ans = min(ans, total_ones - cur_ones)
        return ans