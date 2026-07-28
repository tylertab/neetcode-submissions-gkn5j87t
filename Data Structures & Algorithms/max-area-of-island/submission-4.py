class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if i not in range(len(grid)):
                return 0
            if j not in range(len(grid[i])):
                return 0
            if grid[i][j] == 0:
                return 0
        
            grid[i][j] = 0
            return dfs(grid, i, j + 1) + \
            dfs(grid, i, j - 1) + \
            dfs(grid, i + 1, j) + \
            dfs(grid, i - 1, j) + \
            + 1
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = max(dfs(grid, i, j), res)
        return res

            