class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = {5:0,10:0,20:0}

        def getbestchange(bill):
            if bill == 20:
                if register[10] > 0 and register[5] > 0:
                    register[10] -= 1
                    register[5] -= 1
                    return True
                elif register[5] > 2:
                    register[5] -= 3
                    return True
                else:
                    return False
            elif bill == 10:
                if register[5] > 0:
                    register[5] -= 1
                else:
                    return False
            else:
                return True
        
        for bill in bills:
            if getbestchange(bill) == False:
                return False
            else:
                register[bill] += 1
        return True

                    

        
            

            
