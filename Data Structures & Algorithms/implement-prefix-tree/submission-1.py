class PrefixTree:

    def __init__(self):
        self.isend = False
        self.children = [None] * 26

    def insert(self, word: str) -> None:
        root = self
        for i in range(len(word)):
            char = word[i]
            index = ord(char)-ord('a')
            if root.children[index] == None:
                root.children[index] = PrefixTree()
            root = root.children[index]
            if i == len(word) - 1:
                root.isend = True


    def search(self, word: str) -> bool:
        root = self
        for i in range(len(word)):
            char = word[i]
            index = ord(char)-ord('a') 
            if root.children[index] == None:
                return False
            root = root.children[index]
            if i == len(word) - 1:
                if root.isend == False:
                    return False
        return True

    def startsWith(self, prefix: str) -> bool:
        root = self
        word = prefix
        for i in range(len(word)):
            char = word[i]
            index = ord(char)-ord('a') 
            if root.children[index] == None:
                return False
            root = root.children[index]
        return True

        
        