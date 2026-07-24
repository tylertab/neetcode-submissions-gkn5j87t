class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #keep track of most frequent letter in the window
        #take this and subtract size of window 
        #to get the amount of changes needed
        #if this amount is greater then k
        #keep removing from window until the amount of changes
        #is less then k
        #result is largest window size
        start = 0
        end = 0
        freq = {}
        res = 0
        mostfreq = 0
        while end < len(s):
            freq[s[end]] = freq.get(s[end], 0) + 1
            mostfreq = max(mostfreq, freq[s[end]])
            changes = end - start + 1 - mostfreq
            if changes > k:
                freq[s[start]] = freq[s[start]] - 1
                start = start + 1
            res = max(res, end - start + 1)
            end = end + 1
        
        return res




        