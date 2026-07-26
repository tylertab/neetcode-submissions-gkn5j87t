class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[-1]
        while l < r:
            m = (r + l) // 2
            if nums[m] <= nums[r]:
                r = m 
                res = min(res, nums[m])
            else:
                l = m + 1
        return res
            
