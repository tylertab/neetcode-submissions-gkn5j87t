class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        start = 0
        mask = 0
        res= 0 
        for end in range(len(nums)):
            curr = nums[end]
            if (mask & curr) == 0:
                mask = (mask | curr)
            else:
                start = end
                mask = curr
            res = max(res, end - start + 1)
        return res