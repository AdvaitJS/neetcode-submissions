class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left = 0 
        right = (col * row) -1  
        while right >= left:
            mid = left + (right - left)//2
            rows = mid //col
            cols = mid % col
            value = matrix[rows][cols]

            if value == target:
                return True
            elif value > target:
                right = mid - 1 
            else:
                left = mid + 1 
        return False