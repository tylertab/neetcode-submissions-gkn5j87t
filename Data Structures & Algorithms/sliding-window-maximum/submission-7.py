import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mh = []
        for i in range(0, k - 1):
            heapq.heappush(mh, (-nums[i], i))
        start = 0
        end = k - 1
        res = []
        while end < len(nums):
            #while heap is not in window, pop()
            heapq.heappush(mh, (-nums[end], end))

            while(mh[0][1] not in range(start, end + 1)):
                heapq.heappop(mh)
            res.append(-mh[0][0])
            end = end + 1
            start = start + 1
        return res
            


