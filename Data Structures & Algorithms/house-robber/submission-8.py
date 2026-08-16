class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp so at each step we can choose to rob or not to rob
        #we can only rob if we don't rob the previous house
        #go through array return max of robbing or not robbing
        #track previous if robbed
        memo = {}
        def dfs(i, pr):
            if i not in range(len(nums)):
                memo[(i,False)] = 0
                memo[(i,True)] = 0
                return 0

            if pr:
                #previous robbed so can't rob
                if (i, True) in memo:
                    return memo[(i, True)]
                dontrob = memo.get((i + 1, False), dfs(i + 1, False))
                memo[(i, True)] = dontrob
                return dontrob
            if not pr:
                #not robbed
                if (i, False) in memo:
                    return memo[(i, False)]
                dontrob = memo.get((i + 1,False), dfs(i + 1, False))
                #rob
                rob = memo.get((i + 1,True), dfs(i + 1, True)) + nums[i]
                memo[(i,False)] = max(rob, dontrob)
                return max(rob, dontrob)

        return dfs(0, False)



