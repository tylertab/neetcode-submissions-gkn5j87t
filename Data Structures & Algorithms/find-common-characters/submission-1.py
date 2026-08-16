class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = {}
        for c in words[0]:
            s[c] = s.get(c,0) + 1
        for word in words:
            ts = {}
            #get freq of curr word
            for c in word:
                ts[c] = ts.get(c,0) + 1
            
            todel = []
            #iterate through common freq
            for c in s:
                #if c not in curr word mark for del
                if c not in ts:
                    todel.append(c)
                #if c in curr word make sure min count is saved
                else:
                    s[c] = min(s[c], ts[c])
            #del not in curr word
            for d in todel:
                del s[d]
            
        res = []
        for c in s:
            res += [c] * s[c] 
        
        return res
            
