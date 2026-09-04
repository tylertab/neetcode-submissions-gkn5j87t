class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordindex = [0]
        visited = set()
        def validroot(i,j):
            if wordindex[0] not in range(len(word)):
                return True
            if i not in range(len(board)):
                return False
            if j not in range(len(board[i])):
                return False
            if (i,j) in visited:
                return False

            curr = board[i][j]
            visited.add((i,j))
            if board[i][j] == word[wordindex[0]]:
                wordindex[0] += 1
                present = validroot(i + 1,j) or \
                validroot(i - 1,j) or \
                validroot(i, j + 1) or \
                validroot(i, j - 1)
                wordindex[0] -= 1
                visited.remove((i,j))
                return present
            else:
                visited.remove((i,j))
                return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    present = validroot(i,j)
                    if present:
                        return True
        return False