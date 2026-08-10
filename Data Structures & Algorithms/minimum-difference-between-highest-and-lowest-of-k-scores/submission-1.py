class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        res = sys.maxsize
        for end in range(k - 1, len(nums)):
            res = min(res, nums[end] - nums[start])
            start += 1
        return res

