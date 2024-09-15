class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        n = len(height)
        arr = []
        for i in range(1, n):
            if height[i - 1] > threshold:
                arr.append(i)
        return arr
