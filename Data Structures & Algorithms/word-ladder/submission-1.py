class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        chars = 'abcdefghijklmnopqrstuvwxyz'
        q = deque([(beginWord, 1)])
        visited = set()
        while len(q) > 0:
            word, level = q.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for c in chars:
                    checkword = word[:i] + c + word[i + 1:]
                    if checkword in wordList and checkword not in visited:
                        visited.add(checkword)
                        q.append((checkword, level + 1))
        return 0
        


                