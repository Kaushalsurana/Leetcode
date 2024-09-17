class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def Reverse(arr,st,end):
            while st<=end:
                arr[st],arr[end]=arr[end],arr[st]
                st+=1
                end-=1
        n=len(nums)
        Reverse(nums,0,n-k-1)
        Reverse(nums,n-k,n-1)
        Reverse(nums,0,n-1)
        