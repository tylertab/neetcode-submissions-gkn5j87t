class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            # mid = (start + end) // 2  
            # print(start, end)      
            if nums[(start + end) // 2] == target:
                return (start + end) // 2
            if nums[(start + end) // 2] < target:
                start = (start + end) // 2 + 1
            elif nums[(start + end) // 2] > target:
                end = (start + end) // 2 - 1

        return -1
