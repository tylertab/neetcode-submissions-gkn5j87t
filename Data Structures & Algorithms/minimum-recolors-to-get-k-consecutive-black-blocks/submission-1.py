class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whitefreq = 0
        for i in range(k):
            if blocks[i] == "W":
                whitefreq += 1
        res = whitefreq
        start = 0
        for end in range(k, len(blocks)):
            if blocks[start] == "W":
                whitefreq -= 1
            start += 1
            if blocks[end] == "W":
                whitefreq += 1
            res = min(res, whitefreq)
        return res
