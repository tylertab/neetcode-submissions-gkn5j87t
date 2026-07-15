class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a mapping of letter count array -> words
        lcm = {} 
        #for word in strs, genereate letter Count arr, save in map
        for w in strs:
            lc = [0] * 26
            for c in w:
                lc[ord(c) - 97] = lc[ord(c) - 97] + 1
            slc = ", ".join(map(str, lc))
            lcm[slc] = lcm.get(slc, []) + [w]
            
        #return letterCountmap values
        return [x for x in lcm.values()]