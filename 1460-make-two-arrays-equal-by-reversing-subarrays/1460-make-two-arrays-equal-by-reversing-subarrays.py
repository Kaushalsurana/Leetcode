class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target)==len(arr):
            target.sort()
            arr.sort()
            return target==arr
        else:
            return False