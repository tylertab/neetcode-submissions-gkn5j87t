class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
        
        for key in freq:
            if freq[key] == 1:
                k -= 1
            if k == 0:
                return key
        return ""