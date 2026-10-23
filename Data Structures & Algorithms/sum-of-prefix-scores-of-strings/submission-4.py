class TrieNode:
    def __init__(self):
        self.ends = 0
        self.children = [None] * 26
class Solution:
    def add_word(self, root: TrieNode, word: str):
        currNode = root
        for c in word:
            index = ord(c) - ord('a')
            if currNode.children[index] == None:
                currNode.children[index] = TrieNode()
            currNode.children[index].ends += 1
            currNode = currNode.children[index]

    def get_score(self, root: TrieNode, word: str):
        currNode = root
        score = 0
        for c in word:
            index = ord(c) - ord('a')
            score += currNode.children[index].ends
            currNode = currNode.children[index]

        return score
        
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        n = len(words)
        res = [0] * n
        root = TrieNode()
        for word in words:
            self.add_word(root, word)
        for i in range(n):
            res[i] = self.get_score(root, words[i])
        return res

            
