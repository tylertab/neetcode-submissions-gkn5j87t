class Solution:
    def maxScore(self, s: str) -> int:
        m = 0
        for i in range(len(s) - 1):
            start = 0
            end = i + 1
            left = s[start:end]
            right = s[end:]
            score = 0
            for c in left:
                if c == "0":
                    score +=1
            for c in right:
                if c == "1":
                    score +=1
            m = max(m,score)
        return m