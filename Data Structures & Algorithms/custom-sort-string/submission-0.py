class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mp = {}
        val = 0
        for c in order:
            mp[c] = val
            val += 1
        s = [c for c in s]
        s.sort(key = lambda x: mp.get(x, sys.maxsize))
        res = ""
        for c in s:
            res += c
        return res
