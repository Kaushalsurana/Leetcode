class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=set(nums1).intersection(set(nums2))
        return min(i) if len(i)>0 else -1