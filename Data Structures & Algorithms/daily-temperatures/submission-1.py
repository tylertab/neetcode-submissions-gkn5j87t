class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = []
        for i in range(len(ans)):
            t = temperatures[i]
            while len(st) != 0:
                top = st[-1]
                topv = temperatures[top]
                if t > topv:
                    ans[top] = i - top
                    st.pop()
                else:
                    break
            st.append(i)
        return ans