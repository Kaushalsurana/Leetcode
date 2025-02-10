class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums, target):
            n = len(nums) # size of the array
            low, high = 0, n - 1

            # Perform the steps:
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return True
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        n = len(matrix)
        m=len(matrix[0])
        print(m)
        for i in range(n):
            if matrix[i][m-1] >= target:  
                if binarySearch(matrix[i], target):
                    return True  
        return False