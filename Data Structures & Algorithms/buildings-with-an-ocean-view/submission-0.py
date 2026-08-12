class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        #So if we have the suffix max at each point we can check if any buildings to right are greater than curr
        #list should be naturally sorted as we go along from right since buildings to left must be larger then to the right to have ocean view.
        #just keep track of max going backwards:
        #push into front of list 
        m = 0
        res = []
        for i in range(n - 1, -1, -1):
            if heights[i] > m:
                res.insert(0, i)
                m = heights[i]
        return res