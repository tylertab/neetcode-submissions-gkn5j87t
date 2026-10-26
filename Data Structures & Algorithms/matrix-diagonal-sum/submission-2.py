class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        ans = 0
        i = 0
        j = 0
        while i < m and j < m:
            ans += mat[i][j]
            i += 1
            j += 1
        i = 0
        j = m - 1
        while i >= 0 and j >= 0:
            ans += mat[i][j]
            i += 1
            j -= 1
        if m % 2 != 0:
            ans -= mat[m // 2][m // 2]
        return ans

