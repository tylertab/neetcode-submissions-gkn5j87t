class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        steps = 0
        while i <= n:
            n -= i
            steps += 1
            i += 1
        return steps