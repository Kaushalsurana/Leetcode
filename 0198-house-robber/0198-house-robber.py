class Solution:
    def rob(self, nums: List[int]) -> int:
        p1 = nums[0]
        n=len(nums)
        p2 = 0    
        for i in range(1, n):
            pick = nums[i]
            if i > 1:
                pick += p2 
            non_pick = 0 + p1
            cur_i = max(pick, non_pick)
            p2 = p1
            p1 = cur_i
        return p1