class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        while l <= r:
            mid = (l + r) // 2
            n = nums[mid]
            if nums[mid] == target: 
                return mid
            if n < target: 
                if nums[r] < target and nums[r] > n:
                    r = mid - 1
                else:
                    l = mid + 1
            else: 
                if nums[l] > target and nums[l] <= n:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

        