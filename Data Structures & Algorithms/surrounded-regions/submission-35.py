class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        m, n = len(board), len(board[0])
        def dfs(i, j):
            stack = [(i,j)]
            while len(stack) > 0:
                i, j = stack.pop()
                if not (0 <= i < m and 0 <= j < n):
                    continue
                if board[i][j] == 'X':
                    continue
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                stack.extend([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])

        for i in range(m):
            for j in (0, n - 1):
                if board[i][j] == 'O':
                    dfs(i, j)
        for j in range(n):
            for i in (0, m - 1):
                if board[i][j] == 'O':
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'

                
