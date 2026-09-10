class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        pd = lambda a,b,c,d: (a * b) - (c * d)
        maximum = list(map(lambda x: -x, nums))
        heapq.heapify(maximum)
        minimum = nums
        heapq.heapify(minimum)

        minproduct = heapq.heappop(minimum) * heapq.heappop(minimum)
        maxproduct = heapq.heappop(maximum) * heapq.heappop(maximum)

        return maxproduct - minproduct


