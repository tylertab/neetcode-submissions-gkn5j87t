class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = ""
        counto = 0
        countc = 0
        for l in s:
            if l == '(':
                stack.append(l)
            elif l == ')':
                if stack != []:
                    if stack[-1] == '(':
                        stack.pop(-1)
                        counto += 1
                        countc += 1
        res = ""
        for l in s:
            if l == '(':
                if counto > 0:
                    res += (l)
                    counto -= 1
            elif l == ')':
                if countc > 0 and countc > counto:
                    res += (l)
                    countc -= 1
            else:
                res += (l)
        return res


