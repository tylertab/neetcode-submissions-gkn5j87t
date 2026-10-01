class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        curr = []
        def backtrack(k, n):
            if len(curr) == k:
                out.append(curr.copy())
                return
            if n == 0:
                return 
            curr.append(n)
            backtrack(k, n - 1)
            curr.pop(-1)
            backtrack(k, n - 1)

        backtrack(k,n)
        return out
            