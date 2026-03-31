class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seenSets = {}
        for s in strs:
            h = hash(frozenset(Counter(s).items()))
            if h in seenSets:
                seenSets[h].append(s)
            else:
                seenSets[h] = [s]

        return list(seenSets.values())