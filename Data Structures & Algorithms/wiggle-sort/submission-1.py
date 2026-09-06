class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        lessThan = True

        for i in range(len(nums) - 1):
            if lessThan and nums[i] > nums[i + 1]:
                swap(i, i + 1)
            elif not lessThan and nums[i] < nums[i + 1]:
                swap(i, i + 1)
            lessThan = not lessThan
        return nums
            