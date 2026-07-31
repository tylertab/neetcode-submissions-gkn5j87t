import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return math.sqrt((x * x) + (y * y))
        heap = []
        for point in points:
            d = dist(point[0],point[1])
            heapq.heappush(heap,(d,point))
        res = []
        while k > 0 and len(heap) > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res