class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer1 = 0
        if s == "":
            return True
        for c in t:
            if c == s[pointer1]:
                pointer1 += 1
            if pointer1 == len(s):
                return True
        return False

            