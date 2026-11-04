class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {}
        
        for i in range(len(order)):
            mp[order[i]] = i
        
        def compare(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
                c = word1[i]
                c2 = word2[i]
                i += 1
                if mp[c] == mp[c2]:continue
                else: return mp[c] - mp[c2]

            return len(word1) - len(word2)
        
        for i in range(1, len(words)):
            j = i - 1
            if compare(words[i],words[j]) < 0:
                return False

        return True

        