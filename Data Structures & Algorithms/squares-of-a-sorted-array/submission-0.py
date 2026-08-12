class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0 
        right = n - 1
        res = [0] * n
        pointer = n - 1
        while left <= right:
            leftav = abs(nums[left])
            rightav = abs(nums[right])

            if leftav > rightav:
                res[pointer] = leftav * leftav
                pointer -= 1
                left += 1
            else:
                res[pointer] = rightav * rightav
                pointer -= 1
                right -= 1
        return res
