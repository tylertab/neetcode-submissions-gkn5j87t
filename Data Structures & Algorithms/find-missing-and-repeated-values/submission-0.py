class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set()
        res = [-1,-1]
        n = len(grid)
        for row in range(n):
            for col in range(n):
                num = grid[row][col]
                if num in s:
                    res[0] = num
                s.add(num)
                    
        for i in range(1, (n * n) + 1):
            if i not in s:
                res[1] = i
                return res
