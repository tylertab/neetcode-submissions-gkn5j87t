class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def containsfreq(wf, f):
            for c in f:
                if freq[c] > wf.get(c,0):
                    return False
            return True
        if len(s) < len(t):
            return ""
        freq = {}
        for c in t:
            freq[c] = freq.get(c,0) + 1

        res = ""
        wf = {}
        start = 0
        end = 0
        while end < len(s):
            wf[s[end]] = wf.get(s[end], 0) + 1
            
            while containsfreq(wf,freq):
                ws = end - start + 1
                if ws < len(res) or res == "":
                    res = s[start: end + 1]
                wf[s[start]] = wf.get(s[start], 0) - 1
                start = start + 1
            end = end + 1
            
        return res
            
            
            
        

                

