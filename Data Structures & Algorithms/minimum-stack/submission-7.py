class MinStack:

    def __init__(self):
        self.arr = []
        self.pre = []
    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.pre) == 0:
            self.pre.append(val)
        else:
            self.pre.append(min(val,self.pre[-1]))

    def pop(self) -> None:
        self.pre.pop()
        return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.pre[-1]

        
