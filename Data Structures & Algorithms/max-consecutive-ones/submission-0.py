class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                count = 1
                i += 1
                while i < len(nums) and nums[i] == 1:
                    count += 1
                    i += 1
                m = max(m, count)
            i += 1
        return m