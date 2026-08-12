class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        for i in range(n - 1):
            lefteven = nums[i] % 2 == 0
            righteven = nums[i + 1] % 2 == 0
            if lefteven ^ righteven == 0:
                return False
        return True
