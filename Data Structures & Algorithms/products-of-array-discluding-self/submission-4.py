class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(nums) - 1, 0, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        ans = [None] * len(nums)
        print(prefix,suffix,nums)
        for i in range(len(nums)):
            ans[i] = prefix[i] * suffix[i+1]
        return ans
            


        


        

