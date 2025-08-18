class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return nums1
        for i in range(m,m+n):
            nums1[i]=nums2[i-m]
        if nums1[m-1]<nums1[m]:
            return nums1
        return nums1.sort()