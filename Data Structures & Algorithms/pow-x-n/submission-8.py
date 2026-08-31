class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        
        if x == 1:
            return 1
        if x == -1:
            if n % 2 == 0:
                return 1
            if n % 2 == 1:
                return -1
        if n > 0:
            while n != 0:
                res *= x
                n -= 1
            
        elif n < 0:
            while n != 0:
                res /= x
                n += 1
                if res == 0:
                    return res
        return res