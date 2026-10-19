class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        seen = set()
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        def dfs(i,j,prev):
            if i >= m or j >= n or i < 0 or j < 0:
                return 0
            curr = matrix[i][j]
            if curr <= prev:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            seen.add((i,j))
            up = 1 + dfs(i + 1, j,curr)
            down = 1 + dfs(i - 1, j,curr)
            left = 1 + dfs(i, j - 1, curr)
            right = 1 + dfs(i, j + 1, curr)
            seen.remove((i,j))
            memo[(i,j)] = max(up,left,down,right)
            return memo[(i,j)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j,-1))
        return res

