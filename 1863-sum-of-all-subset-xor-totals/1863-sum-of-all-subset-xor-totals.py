class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        for subset in range(1 << n):
            current_xor = 0
            
            for i in range(n):
                if subset & (1 << i):
                    current_xor ^= nums[i]
            total_sum += current_xor
        
        return total_sum