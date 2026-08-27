class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        mp = {}

        for i in range(len(strs)):
            s = strs[i]
            ones = 0
            zeros = 0
            for c in s:
                if c == "1":
                    ones += 1
                else:
                    zeros += 1
            mp[i] = (zeros, ones)

        memo = {}


        def helper(i, lm, ln):
            if lm < 0 or ln < 0:
                return -1
            if i not in range(len(strs)):
                return 0
            if (i, lm, ln) in memo:
                return memo[(i, lm, ln)]
            cm,cn = mp[i]
            

            skip = helper(i + 1, lm ,ln)
            buy = helper(i + 1, lm - cm ,ln - cn) + 1

            memo[(i, lm, ln)] = max(buy,skip)
    
            return max(buy, skip)

        return helper(0, m, n)



      