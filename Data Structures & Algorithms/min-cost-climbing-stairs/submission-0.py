class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #options at each step we can take one step or 2 step
        memo = {}
        def calc(i):
            if i not in range(len(cost)):
                return 0
            if i in memo:
                return memo[i]
            #option 1 one step
            op1 = cost[i] + calc(i + 1)

            op2 = cost[i] + calc(i + 2)
            memo[i] = min(op1, op2)
            return min(op1, op2)
        
        return min(calc(0), calc(1))