class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c =len(matrix[0]) 
        ro = len(matrix)
        l = 0
        r =(ro * c) - 1
        while l <= r:
            mid = (r + l) // 2
            row = mid // c
            col = mid % c
            
            n = matrix[row][col]
            print(mid, row, col, n)
            if n == target:
                return True
            if n < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return False