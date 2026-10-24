class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        seen = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == 0:
                return
            if (i,j) in seen:
                return
            seen.add((i,j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        


        for i in [0, m - 1]:
            for j in range(n):
                if (i,j) not in seen and grid[i][j] == 1:
                    dfs(i, j)

        for i in range(1, m - 1):
            for j in [0,n - 1]:
                if (i,j) not in seen and grid[i][j] == 1:
                    dfs(i, j)

        print(seen)
        count = 0
        for i in range(m):
            for j in range(n):
                if (i,j) in seen or grid[i][j] == 0:
                    continue
                else:
                    count += 1
        return count
                
