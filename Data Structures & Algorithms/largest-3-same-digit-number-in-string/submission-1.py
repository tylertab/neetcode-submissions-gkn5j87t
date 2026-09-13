class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) < 3:
            return ""
        freq = {}

        def add(l):
            freq[l] = freq.get(l, 0) + 1
        def dele(l):
            freq[l] -= 1
            if freq[l] == 0:
                del freq[l]
        
        for i in range(3):
            add(num[i])
        i = 2   
        m = None
        while i < len(num):
            if len(freq) == 1:
                if m == None:
                    m = num[i]
                m = max(m, num[i])
            i += 1
            dele(num[i - 3])
            if i < len(num):
                add(num[i])
        if m == None:
            return ""
        return m + m + m