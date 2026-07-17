class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        cars = [None] * len(position)
        for i in range(len(cars)):
            cars[i] = (position[i], speed[i])

        cars = sorted(cars, key = lambda x: x[0], reverse=True)

        for c in cars:
            t = (target - c[0]) / c[1]
            if len(st) == 0:
                st.append(t)
            else:
                top = st[-1]
                if t > top:
                    st.append(t)
        return len(st)

                