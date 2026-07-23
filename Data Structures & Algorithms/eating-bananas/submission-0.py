class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mp = 0 
        for p in piles:
            mp = max(mp, p)
        l = 1
        r = mp
        res = mp
        while l <= r: 
            mid = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
                res = mid
            
        return res
