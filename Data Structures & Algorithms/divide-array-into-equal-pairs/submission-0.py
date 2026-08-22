class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for value in list(freq.values()):
            if value % 2 != 0:
                return False
        return True