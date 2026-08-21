class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        m = 0
        for n in nums:
            freq[n] = freq.get(n,0) + 1
            if freq[n] > freq.get(m, 0):
                m = n

        return m