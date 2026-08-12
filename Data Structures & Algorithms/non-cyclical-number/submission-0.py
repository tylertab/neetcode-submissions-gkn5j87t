class Solution:
    def isHappy(self, n: int) -> bool:
        def replace(n):
            s = 0
            while n != 0:
                d = n % 10
                s += d * d
                n = n // 10

            return s
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = replace(n)
        return True
