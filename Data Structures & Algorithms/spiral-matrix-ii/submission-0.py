class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0 for _ in range(n)] for _ in range(n)]
        curr = 1
        border = 0

        while curr <= (n * n):
            for col in range(border,n - border):
                m[border][col] = curr
                if curr == (n*n):
                    break
                curr += 1

            if curr == (n*n):
                break
            for row in range(border + 1, n - border - 1):
                m[row][n - border - 1] = curr
                curr +=1
                print(row,m[row])
        
            for col in range(n-border-1,border - 1,-1):
                m[n-border-1][col] = curr
                curr += 1
                print(border,n-border-1,m[n-border-1])

            for row in range(n - border - 2,border, -1):
                m[row][border] = curr
                curr += 1
                print(border,row,m[row])

            border += 1
            

        return m
