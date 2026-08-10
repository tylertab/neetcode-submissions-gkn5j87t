import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        #(o(n))
        gifts = list(map(lambda x: -x, gifts))
        #(o(n))
        heapq.heapify(gifts)

        while len(gifts) > 0 and k != 0:
            largestpile = -heapq.heappop(gifts)
            heapq.heappush(gifts,-floor(math.sqrt(largestpile)))
            k -= 1
        return sum(list(map(lambda x: -x,gifts)))

