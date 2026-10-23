class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        firstseen = {}
        for i in range(len(s)):
            c = s[i]
            if c not in firstseen:
                firstseen[c] = i
            else:
                res = max(res, i - firstseen[c] - 1)

        return res