class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        
        pi = 0
        ni = 0
        for i in range(len(nums)):
            value = None
            if i % 2 == 0:
                value = pos[pi]
                pi += 1
            else:
                value = neg[ni]
                ni += 1

            nums[i] = value
        return nums