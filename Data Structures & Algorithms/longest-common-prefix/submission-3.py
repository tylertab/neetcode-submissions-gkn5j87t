class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        while True:
            c = None
            for word in strs:
                if i not in range(len(word)):
                    return res
                if c is None:
                    c = word[i]
                    continue
                if word[i] != c:
                    return res
            i += 1
            res += c
        return res