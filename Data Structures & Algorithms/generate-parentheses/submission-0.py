class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #options 
        #close perentece
        #add open perentece
        out = []
        def helper(o, c, curr):
            if c == n:
                out.append(curr)
                return
            if o == 0:
                helper(o + 1, c, curr + "(")
            else:
                if o == n:
                    helper(o, c + 1, curr + ")")
                else:
                    helper(o + 1, c, curr + "(")
                    if o != 0 and o > c:
                        helper(o, c + 1, curr + ")")
        
        helper(0,0,"")
        return out
            

            
