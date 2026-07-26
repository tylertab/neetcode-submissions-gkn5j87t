class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[-1]
        while l <= r:
            m = (r + l) // 2
            res = min(res, nums[m])

            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
        return res
            
