class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        comb = []
        val = 0
        def dfs(i, val):
            if i >= len(nums) or val >target:
                return
            if val == target:
                if comb not in res:
                    res.append(comb.copy())
                return
            comb.append(nums[i])
            val += nums[i]
            dfs(i, val)
            dfs(i + 1,val)

            comb.pop()
            val -= nums[i]
            dfs(i + 1,val)
        dfs(0,val)
        return res