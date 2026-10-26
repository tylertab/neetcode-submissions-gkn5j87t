class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == ',': continue
            if c != ')':
                stack.append(c)
                continue
            yes = no = False
            while stack[-1] != '(':
                v = stack.pop()
                yes |= v == 't'
                no |= v == 'f'
            stack.pop()
            op = stack.pop()
            value = not yes if op == '!' else (not no if op == '&' else yes)
            stack.append('t' if value else 'f')
        return stack[0] == 't'

                




        

                
                



                        

            
            
