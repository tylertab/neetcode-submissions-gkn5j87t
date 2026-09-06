class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        res = -1
        for num in freq:
            if num == freq[num] and num > res:
                res = num
        return res
