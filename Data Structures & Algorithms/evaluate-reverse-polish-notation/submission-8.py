class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = set(["+","-","/","*"])
        for t in tokens:
            print(st)
            if t in op:
                n1 = st.pop()
                n2 = st.pop()
                if t == "+":
                    st.append(n1 + n2)
                if t == "-":
                    st.append(n2 - n1)
                if t == "*":
                    st.append(n1 * n2)
                if t == "/":
                    st.append(int((n2 / n1)))
            else:
                st.append(int(t))
        return st.pop()
