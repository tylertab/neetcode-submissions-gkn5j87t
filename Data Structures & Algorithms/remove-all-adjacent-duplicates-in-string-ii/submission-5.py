class Solution:
    class Stack:
        def __init__(self, k):
            self.stack = []
            self.k = k
        def push(self,l):
            stack = self.stack
            stack.append(l)
            while self.topksame():
                self.deltopk()
        def topksame(self):
            stack = self.stack
            k = self.k
            if len(stack) >= k:
                l = None
                for i in range(k):
                    ind = len(stack) - i - 1
                    if l == None:
                        l = stack[ind]
                    else:
                        if l != stack[ind]:
                            return False
                return True
            return False
        def deltopk(self):
            stack = self.stack
            k = self.k
            for i in range(k):
                stack.pop(-1)
        def toString(self):
            return "".join(self.stack)
    def removeDuplicates(self, s: str, k: int) -> str:
        
        
        stack = self.Stack(k)
        for l in s:
            stack.push(l)
        return stack.toString()
                        

                        




            
            

            
            