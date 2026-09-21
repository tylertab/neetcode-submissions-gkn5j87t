class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        haspref = lambda x: x[:len(pref)] == pref
        c = 0
        for word in words:
            if haspref(word):
                c += 1
        return c