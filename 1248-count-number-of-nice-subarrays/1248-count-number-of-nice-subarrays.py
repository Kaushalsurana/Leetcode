class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        a = 0
        b = 0
        c = 0
        d = 0
        for end in range(len(nums)):
            if nums[end] % 2 == 1:
                b += 1
                d = 0
            while b == k:
                if nums[a] % 2 == 1:
                    b -= 1
                d += 1
                a += 1
            c += d
        return (c)
