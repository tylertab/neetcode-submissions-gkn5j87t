class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        m = 0
        for i in range(len(heights)):
            if len(st) == 0: 
                st.append((i,heights[i]))
                continue
            if heights[i] < st[-1][1]:
                j = st[-1][0]
                while len(st) != 0 and heights[i] < st[-1][1]:
                    m = max(m, (i - st[-1][0]) * st[-1][1])
                    j = st.pop()[0]
                st.append((j, heights[i]))
            elif heights[i] > st[-1][1]:
                st.append((i, heights[i]))
        
        while len(st) != 0:
            m = max(m, (len(heights) - st[-1][0]) * st[-1][1])
            st.pop()

        return m

            

                

            
