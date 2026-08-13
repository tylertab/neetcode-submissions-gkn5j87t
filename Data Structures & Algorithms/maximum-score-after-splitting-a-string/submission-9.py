class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        prefix = [0] * n
        suffix  = [0] * n
        su = 0
        for i in range(n):
            prefix[i] = su
            if s[i] == "0":
                su += 1

        su = 0
        for i in range(n-1,-1,-1):
            suffix[i] = su
            if s[i] == "1":
                su += 1
        m = 0
        for i in range(n - 1):
            left = prefix[i + 1]
            right = suffix[i]
            m = max(m, left + right)
        return m

            