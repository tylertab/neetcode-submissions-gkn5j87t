class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(grid, i, j, dist):
            if i not in range(len(grid)):
                return None
            if j not in range(len(grid[i])):
                return None

            

            if grid[i][j] == -1:
                return None
            if grid[i][j] < dist:
                return None
            else:
                grid[i][j] = dist
            dfs(grid, i + 1, j, dist + 1)
            dfs(grid, i - 1, j, dist + 1)
            dfs(grid, i, j + 1, dist + 1)
            dfs(grid, i, j - 1, dist + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    dfs(grid,i,j,0)
        
                