class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in range(k):
            heapq.heappush(minheap,nums[i])
        for i in range(k,len(nums)):
            if nums[i] > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap,nums[i])
            
        return heapq.heappop(minheap)

                