class Solution:
    def minOperations(self, s: str) -> int:
        #option 1 10101
        #option 2 0101010

        def option(boo):
            shouldbezero = boo
            count = 0
            for c in s:
                if c == "0" and shouldbezero == False:
                    count += 1
                if c == "1" and shouldbezero == True:\
                    count += 1
                shouldbezero = not shouldbezero
            return count
        
        zerostart = option(True)
        onestart = option(False)
        return min(zerostart, onestart)
            
                
