class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lcm = {} #letterCountMapping
        for c in s: #for char in string s
            lcm[c] = lcm.get(c, 0) + 1 #c: #c + 1
        for c in t: #for chat in string t
            if c not in lcm:
                return False
            lcm[c] = lcm.get(c) - 1
            if lcm[c] == 0:
                del lcm[c]
            
        if len(lcm) == 0:
            return True
        return False
            


