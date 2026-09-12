class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums) - 1:
            if not nums[i] <= nums[i + 1]:
                break
            i += 1
        if i == len(nums) - 1:
            return True
        i += 1
        while i < len(nums) - 1:
            if not nums[i] <= nums[i + 1]:
                break
            i += 1
        if not i == len(nums) - 1:
            return False
        return nums[-1] <= nums[0]