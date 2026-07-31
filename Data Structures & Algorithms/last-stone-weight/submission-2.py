import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            print(stones)
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            print(x,y)
            if x == y:
                continue
            elif x < y:
                y -= x
                heapq.heappush(stones,-y)
            elif x > y:
                x -= y
                heapq.heappush(stones,-x)
            else:
                heapq.heappush(stones,-x)
                heapq.heappush(stones,-y)
        if (len(stones) is 0):
            return 0
        return  -heapq.heappop(stones)