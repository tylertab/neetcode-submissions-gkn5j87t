class Trie:
    def __init__(self):
        self.isEnd = False
        self.children = {}
    def add_word(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.isEnd = True

class Solution:
    #use a Trie
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.add_word(w)
        
        m, n = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(i, j, node, word):
            if i < 0 or j < 0 or i == m or j == n:
                return
            if (i,j) in visit:
                return
            if board[i][j] not in node.children:
                return
            visit.add((i,j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.isEnd:
                res.add(word)
            
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)

            visit.remove((i,j))


        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        return list(res)