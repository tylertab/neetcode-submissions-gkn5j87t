class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        def shifttoend(index):
            while index + 1 <= k:
                temp = nums[index + 1]
                nums[index + 1] = nums[index]
                nums[index] = temp
                index += 1
        i = 1
        while i + 1 < k:
            while nums[i] == nums[i - 1 ] and nums[i] == nums[i + 1] and i + 1 < k:
                k -= 1
                shifttoend(i + 1)
            i += 1
        
        return k

            
