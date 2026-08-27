class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)
        temp = money
        money -= heapq.heappop(prices)
        money -= heapq.heappop(prices)
        if money < 0:
            return temp
        return money