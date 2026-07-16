class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * (len(height))
        suffix = [0] * (len(height))
        m = 0
        for i in range(len(prefix)):
            prefix[i] = m
            m = max(m, height[i])
        m = 0
        for i in range(len(suffix) - 1, -1, -1):
            suffix[i] = m
            m = max(m, height[i])
        print(prefix, suffix, height)
        
        trapped = 0;
        for i in range(len(prefix)):
            trapped += max(min(prefix[i], suffix[i]) - height[i], 0)
        return trapped

        