class Solution:
    def maxScore(self, s: str) -> int:
        m = 0
        n = len(s)
        for i in range(n - 1):
            left = range(0, i + 1)
            right = range(i + 1, n)
            score = 0
            for c in left:
                if s[c] == "0":
                    score +=1
            for c in right:
                if s[c] == "1":
                    score +=1
            m = max(m,score)
        return m