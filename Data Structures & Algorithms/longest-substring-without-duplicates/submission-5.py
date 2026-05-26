class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        curr = 0
        window = set()
        ls = {}
        i = 0
        while i < len(s):
            if s[i] in window:
                window = set()
                maxi = max(curr,maxi)
                curr = 0
                i = ls[s[i]] + 1
            window.add(s[i])
            curr += 1
            ls[s[i]] = i
            i += 1

        maxi = max(curr,maxi)
        return maxi