class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxK: int) -> int:

        res = 0
        b = l = r= -1
        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                b = i

            if num == mink:
                l = i

            if num == maxK:
                r = i

            res += max(0, min(l, r) - b)

        return res