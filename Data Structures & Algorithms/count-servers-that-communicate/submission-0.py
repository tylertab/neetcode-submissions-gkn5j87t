class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Number of rows
        m = len(grid)
        # Number of columns
        n = len(grid[0])
        # Count servers in each row
        row_count = [0] * m
        # Count servers in each column
        col_count = [0] * n
        # Count the servers in every row and column
        for r in range(m):
            for c in range(n):
                # If there is a server
                if grid[r][c] == 1:
                    # Add one to this row
                    row_count[r] += 1
                    # Add one to this column
                    col_count[c] += 1

        # This will store our answer
        answer = 0
        # Go through every cell again
        for r in range(m):
            for c in range(n):
                # We only care about cells containing servers
                if grid[r][c] == 1:
                    # If there is another server in the same row
                    # OR another server in the same column,
                    # this server can communicate.
                    if row_count[r] > 1 or col_count[c] > 1:
                        answer += 1

        return answer