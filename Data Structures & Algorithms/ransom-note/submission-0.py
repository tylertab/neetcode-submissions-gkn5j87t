class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        for c in magazine:
            freq[c] = freq.get(c, 0) + 1
        for c in ransomNote:
            if freq.get(c, 0) == 0:
                return False
            freq[c] -= 1
        return True
        