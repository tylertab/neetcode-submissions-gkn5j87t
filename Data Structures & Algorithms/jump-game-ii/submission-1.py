class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        dp[-1] = 0
        for i in range(len(nums) - 2,-1,-1):
            if nums[i] == 0:
                dp[i] = sys.maxsize
            else:
                if nums[i] + i >= len(nums):
                    dp[i] = 1
                else:
                    dp[i] = 1 + min(dp[i + 1: i + nums[i] + 1])
        print(dp)
        return dp[0]