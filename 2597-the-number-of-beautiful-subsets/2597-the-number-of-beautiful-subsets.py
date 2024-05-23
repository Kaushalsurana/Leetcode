class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        length = len(nums)
        result = 0
        
        def dfs(index, count_map):
            nonlocal result
            if index == length:
                if count_map:
                    result += 1
                return
            if nums[index] - k not in count_map and nums[index] + k not in count_map:
                count_map[nums[index]] += 1
                dfs(index + 1, count_map)
                count_map[nums[index]] -= 1
                if count_map[nums[index]] == 0:
                    del count_map[nums[index]]
            dfs(index + 1, count_map)
        
        dfs(0, Counter())
        return result