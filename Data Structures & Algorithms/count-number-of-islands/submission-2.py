class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid,i,j):
            if i not in range(0, len(grid)):
                return None
            if j not in range(0,len(grid[0])):
                return None
            if grid[i][j] == "0":
                return None
            if grid[i][j] == "1":
                grid[i][j] = "0"
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1":
                    count = count + 1
                    dfs(grid,i,j)
        return count