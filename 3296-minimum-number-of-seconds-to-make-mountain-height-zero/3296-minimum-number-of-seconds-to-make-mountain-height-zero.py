class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def reducetime(maxTime: int) -> bool:
            t = 0
            for i in workerTimes:
                current = 0
                low, high = 0, mountainHeight
                while low <= high:
                    mid = (low + high) // 2
                    if i * mid * (mid + 1) // 2 <= maxTime:
                        current = mid
                        low = mid + 1
                    else:
                        high = mid - 1
                t += current
                if t >= mountainHeight:
                    return True
            return t >= mountainHeight
        
        left, right = 1, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        while left < right:
            mid = (left + right) // 2
            if reducetime(mid):
                right = mid
            else:
                left = mid + 1
        return left