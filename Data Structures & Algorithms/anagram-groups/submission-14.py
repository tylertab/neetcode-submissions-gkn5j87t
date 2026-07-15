class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag = {} #frequencyMap -> words

        for word in strs:
            lc = [0] * 26
            for c in word:
                lc[ord(c) - 97] = lc[ord(c) - 97] + 1
            k = " ".join(str(x) for x in lc)
            ag[k] = ag.get(k,[]) + [word]
           
        return [x for x in ag.values()] 