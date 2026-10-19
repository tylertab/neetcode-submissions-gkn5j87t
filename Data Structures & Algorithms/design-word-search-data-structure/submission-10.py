class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isEndOfWord = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a') 
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(curr, i):
            #if i is len(word) curr must represent last letter
            if i == len(word):
                if curr.isEndOfWord:
                    return True
                return False
            #print(word[i])
            #if c is . we want to dfs from every node
            if word[i] == '.':
                for node in curr.children:
                    if node != None:
                        if dfs(node, i + 1):
                            return True
                return False
            #if c is not . does it exist as a child ?
            else:
                index = ord(word[i]) - ord('a')
                if curr.children[index] == None:
                    return False
                else:
                    return dfs(curr.children[index], i + 1)
        
        return dfs(curr, 0)
