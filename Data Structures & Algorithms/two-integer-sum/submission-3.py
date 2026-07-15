class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ntim = {} #numToIndexMappings
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in ntim:
                return [ntim[complement], i]
            ntim[nums[i]] = i
