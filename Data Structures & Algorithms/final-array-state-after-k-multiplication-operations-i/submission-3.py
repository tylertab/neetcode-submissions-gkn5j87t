class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
        heapq.heapify(nums)
        while k != 0:
            val, index = heapq.heappop(nums)

            heapq.heappush(nums, (val * multiplier, index))
            k-=1
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            itemval, itemind = nums[i]
            res[itemind] = itemval


        return res
