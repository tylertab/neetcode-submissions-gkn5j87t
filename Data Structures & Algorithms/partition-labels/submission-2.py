class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i in range(len(s)):
            last[ord(s[i]) - ord('a')] = i
        
        res = []
        curr = 0
        end = 0
        for i in range(len(s)):
            l = last[ord(s[i]) - ord('a')]
            if l > end:
                end = l
            curr += 1
            if end <= i:
                res.append(curr)
                curr = 0
                end = end + 1
        return res



