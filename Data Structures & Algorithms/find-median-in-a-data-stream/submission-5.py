class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        large = self.large
        small = self.small
        if len(large) != 0 and num > large[0]:
            heapq.heappush(large,num)
        else:
            heapq.heappush(small,-num)
        if len(large) > len(small) + 1:
            heapq.heappush(small, -heapq.heappop(large))
        elif len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        

    def findMedian(self) -> float:
        large = self.large
        small = self.small
        if len(large) > len(small):
            return large[0]
        if len(small) > len(large):
            return -small[0]
        return (-small[0] + large[0]) / 2
        
        