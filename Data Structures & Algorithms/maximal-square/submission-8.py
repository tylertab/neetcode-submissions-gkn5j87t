class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    continue
                left = up = diag = 0
                if j > 0: left = dp[i][j - 1]
                if i > 0: up = dp[i - 1][j]
                if i > 0 and j > 0: diag = dp[i - 1][j - 1]
                
                dp[i][j] = 1 + min([left, up, diag])
                res = max(res, dp[i][j])
        return res * res
