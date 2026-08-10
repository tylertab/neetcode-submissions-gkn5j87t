class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count = 0
        if t == "":
            return count
        pointer1 = 0
        for c in s:
            if c == t[pointer1]:
                pointer1 += 1
            if pointer1 == len(t):
                return count
        return len(t) - pointer1