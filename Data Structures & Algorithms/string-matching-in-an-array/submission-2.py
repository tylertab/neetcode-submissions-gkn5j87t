class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        out = set()
        for i in range(len(words)):
            curr = words[i]
            for j in range(len(words)):
                if j == i:
                    continue
                if words[j] in curr:
                    out.add(words[j])
        
        return [x for x in out]
                    
            