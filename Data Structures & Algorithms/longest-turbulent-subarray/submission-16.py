class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        signs = []
        if len(arr) == 1:
            return 1
        def findsigns(i):
            while i + 1 < len(arr):
                if arr[i] < arr[i+1]:
                    signs.append('<')
                if arr[i] > arr[i + 1]:
                    signs.append('>')
                if arr[i] == arr[i + 1]:
                    signs.append('=')
                if signs[-1] == '=':
                        signs.pop()
                        return i + 1
                if len(signs) > 1:
                    if signs[-1] == '<' and signs[-2] != '>':
                        signs.pop()
                        return i
                    if signs[-1] == '>' and signs[-2] != '<':
                        signs.pop()
                        return i
                i += 1
            return i
            

        i = 0
        m = 0
        while i < len(arr) - 1:
            i = findsigns(i)
            m = max(m, len(signs) + 1)
            signs = []
        return m




            
            

            

