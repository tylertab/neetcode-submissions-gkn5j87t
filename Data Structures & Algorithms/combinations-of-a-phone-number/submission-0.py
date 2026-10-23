class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mp = {
        }
        curr = ord('a')
        for i in range(2,10):
            ite = 3
            if i == 7 or i == 9:
                ite = 4
            for _ in range(ite):
                mp[str(i)] = mp.get(str(i),[]) + [chr(curr)]
                curr += 1

        if len(digits) == 0:
            return res

        def dfs(i, s):
            if i == len(digits):
                res.append(s)
                return
            letters = mp[digits[i]]
            for l in letters:
                dfs(i + 1, s + l)
        

        dfs(0, "")
        return res