class Solution:
    def maxScore(self, s: str) -> int:
        m = 0
        for i in range(len(s) - 1):
            start = 0
            end = i + 1
            left = range(start, end)
            right = range(end, len(s))
            score = 0
            for c in left:

                if s[c] == "0":
                    score +=1
            for c in right:
                if s[c] == "1":
                    score +=1
            m = max(m,score)
        return m