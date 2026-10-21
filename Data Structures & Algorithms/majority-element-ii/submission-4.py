class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        if len(nums) == 2:
            return list(set(nums))
        heapq.heapify(nums)

        n = len(nums)
        res = []
        currcount = 1
        prev = heapq.heappop(nums)
        while len(nums) > 0:
            curr = heapq.heappop(nums)
            if curr == prev:
                currcount += 1
                if currcount > n // 3:
                    res.append(curr)
                    while prev == curr and len(nums) > 0:
                        prev = curr
                        curr = heapq.heappop(nums)
                    currcount = 1
            else:
                currcount = 1
            prev = curr
        return res