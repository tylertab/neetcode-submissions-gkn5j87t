class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        
        global_max = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            
            # When multiplying by a negative number, max and min values swap roles.
            # We can temporarily store curr_max or compute all 3 candidates at once.
            temp_max = max(num, curr_max * num, curr_min * num)
            curr_min = min(num, curr_max * num, curr_min * num)
            
            curr_max = temp_max
            
            # Update the overall maximum product found so far
            global_max = max(global_max, curr_max)

        return global_max