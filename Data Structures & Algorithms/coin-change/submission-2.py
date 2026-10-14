class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            m = sys.maxsize
            for coin in coins:
                if amount - coin >= 0:
                    m = min(1 + dfs(amount - coin),m)
            memo[amount] = m
            return m
        minCoins = dfs(amount)
        return -1 if minCoins >= sys.maxsize else minCoins