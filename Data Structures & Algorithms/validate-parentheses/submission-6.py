class Solution:
    def isValid(self, s: str) -> bool:
        com = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        st = []
        for c in s:
            if c not in com:
                st.append(c)
            else:
                if len(st) == 0 or com[c] != st.pop():
                    return False

        return len(st) == 0




