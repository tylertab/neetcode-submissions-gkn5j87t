class Solution:
    def frequencySort(self, s: str) -> str:
        f = {}
        for c in s:
            f[c] = f.get(c, 0) + 1
        
        heap = [(-v, k) for (k, v) in f.items()]
        heapq.heapify(heap)
        res = ""
        while len(heap) > 0:
            n, c = heapq.heappop(heap)
            for _ in range(-n):
                res += c
        return res


