import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap1 = []
        self.heap2 = []
        for n in nums:
            heapq.heappush(self.heap1, -n)
        for i in range(min(k, len(nums))):
            heapq.heappush(self.heap2, -self.heap1.pop(0))
        self.size = len(nums)
        self.k = k


    def add(self, val: int) -> int:
        if self.size < self.k:
            heapq.heappush(self.heap2, val)
            self.size += 1
        elif val > self.heap2[0]:
            heapq.heappush(self.heap1, heapq.heappop(self.heap2))
            heapq.heappush(self.heap2, val)
        else:
            heapq.heappush(self.heap1, -val)
        return self.heap2[0]

