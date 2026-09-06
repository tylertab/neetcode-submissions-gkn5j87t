class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def single(i):
            if i == 0:
                return nums[i + 1] != nums[i]
            elif i == len(nums) - 1:
                return nums[i - 1] != nums[i]
            else:
                return nums[i + 1] != nums[i] and nums[i - 1] != nums[i]
        
        def checkmid(start, end):
            if start not in range(len(nums)) or end not in range(len(nums)):
                return None
            if start > end:
                return None
            mid = (start + end) // 2
            if single(mid) == True:
                return nums[mid]
            else:
                half2 = checkmid(mid + 1, end)
                half1 = checkmid(start, mid - 1)
                if half1 != None:
                    return half1
                if half2 != None:
                    return half2
    
        return checkmid(0, len(nums) - 1)
