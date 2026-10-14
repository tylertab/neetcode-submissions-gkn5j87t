class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first = {}
        last = {}
        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i
            last[s[i]] = i
        
        res = []
        curr = 0
        end = 0
        for i in range(len(s)):
            l = last[s[i]]
            if l > end:
                end = l
            curr += 1
            if end <= i:
                res.append(curr)
                curr = 0
                end = end + 1
        return res



