class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        high=len(matrix)-1
        while low<=high:
            mid=(high+low)//2
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                break
            if matrix[mid][0]>target:
                high=mid-1
            else:
                low=mid+1
        row=mid
        low=0
        high=len(matrix[0])-1
        while low<=high:
            mid=(high+low)//2
            if matrix[row][mid]==target:
                return True
            if matrix[row][mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False