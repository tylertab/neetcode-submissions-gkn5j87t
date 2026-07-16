class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        m = 0;
        while i < j:
            w = j - i
            h = min(heights[j],heights[i])
            m = max(m, h * w)
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return m

