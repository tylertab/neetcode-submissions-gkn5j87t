class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            for j in range(11):
                if (i & (1 << j)):
                    count += 1
            res.append(count)
        return res
        