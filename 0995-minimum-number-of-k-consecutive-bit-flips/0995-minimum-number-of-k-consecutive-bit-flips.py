class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        a = len(nums)
        b = c = 0
        d = [0] * a

        for i, num in enumerate(nums):
            if i >= k:
                c -= d[i - k]

            if (num == 1 and c % 2 == 0) or (num == 0 and c % 2 == 1):
                continue

            if (num == 1 and c % 2 == 1) or (num == 0 and c % 2 == 0):
                if i + k > a:
                    return -1
                d[i] = 1
                c += 1
                b += 1

        return b