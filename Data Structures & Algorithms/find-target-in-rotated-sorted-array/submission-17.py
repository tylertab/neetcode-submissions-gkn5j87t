class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        while l <= r:
            if nums[(l + r) // 2] == target: 
                return (l + r) // 2
            if nums[(l + r) // 2] < target: 
                if nums[r] < target and nums[r] > nums[(l + r) // 2]:
                    r = ((l + r) // 2) - 1
                else:
                    l = ((l + r) // 2) + 1
            else: 
                if nums[l] > target and nums[l] <= nums[(l + r) // 2]:
                    l = ((l + r) // 2) + 1
                else:
                    r = ((l + r) // 2) - 1
        return -1

        