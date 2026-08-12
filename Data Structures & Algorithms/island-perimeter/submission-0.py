class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #if the island is one block ther perimiter is 4
        #if the block is connected to something, then that side wont be apart of the perimter
        #if the block is surrounded on all 4 sides then there is no perimiter.
        #So we can do a dfs on island
        #we assume the perimeter of the block is 4 and subtract for each nearby block   
        #instead we can dfs the block and everytime we hit a block that is not land
        #we count it as perimiter,

        def dfs(i,j):
            if i not in range(len(grid)):
                return 1
            if j not in range(len(grid[i])):
                return 1
            if  grid[i][j] == 0:
                return 1
            if grid[i][j] == -1:
                return 0
            grid[i][j] = -1
            return dfs(i + 1,j) + dfs(i - 1,j) + dfs(i,j + 1) + dfs(i,j - 1)
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return dfs(row,col)
        return 0
        



            