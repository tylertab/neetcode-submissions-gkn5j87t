class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       n = len(nums)
       s = (int) (n * (1 + n)/2)
       for i in nums:
        s -= i

       return s
