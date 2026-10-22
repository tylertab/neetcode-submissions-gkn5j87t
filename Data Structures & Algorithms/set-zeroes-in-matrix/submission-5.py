class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        firstrowhas = False
        firstcolhas = False
        if 0 in matrix[0]:
            firstrowhas = True
        for i in range(m):
            if matrix[i][0] == 0:
                firstcolhas = True

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for col in range(1, n):
            if matrix[0][col] == 0:
                for row in range(1, m):
                    matrix[row][col] = 0
        for row in range(1, m):
            if matrix[row][0] == 0:
                for col in range(1, n):
                    matrix[row][col] = 0

        if firstrowhas:
            for i in range(n):
                matrix[0][i] = 0
        if firstcolhas:
            for i in range(m):
                matrix[i][0] = 0
        


                
        