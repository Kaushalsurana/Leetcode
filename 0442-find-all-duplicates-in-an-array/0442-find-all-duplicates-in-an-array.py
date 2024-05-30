class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        response = []
        cnt = Counter(nums)
        for k in cnt.keys():
            if cnt[k] > 1:
                response.append(k)
        return response