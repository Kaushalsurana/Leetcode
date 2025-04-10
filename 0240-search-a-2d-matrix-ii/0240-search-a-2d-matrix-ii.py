class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)-1
        col=0
        while row>=0 and col<=len(matrix[0])-1:
            a=matrix[row][col]
            if target>a:
                col+=1
            elif target<a:
                row-=1
            else:
                return True
        return False