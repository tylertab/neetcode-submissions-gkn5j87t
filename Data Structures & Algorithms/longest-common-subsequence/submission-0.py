class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                up = left = diag = 0
                if i > 0: up = dp[i - 1][j]
                if j > 0: left = dp[i][j - 1]
                if i > 0 and j > 0: diag = dp[i - 1][j - 1]
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + diag
                else:
                    dp[i][j] = max(left, up)
        return dp[-1][-1]
