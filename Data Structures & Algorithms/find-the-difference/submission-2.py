class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        for c in t:
            count = freq.get(c, 0)
            if count == 0:
                return c
            freq[c] -= 1
            