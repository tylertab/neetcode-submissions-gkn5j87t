class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        start = 0 
        n = len(nums)
        nums.sort()
        total = nums[0]
        end = 1
        while end < n:
            val = nums[end]
            prefixsize = end - start
            if (prefixsize * val) > (k + total):
                total -= nums[start]
                start += 1
                
            total += val
            end += 1
        return end - start 



