class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                n -= 1
                temp = nums[n]
                nums[n] = nums[i]
                nums[i] = temp
        return n