class MyLinkedList:
    class Node:
        def __init__(self, val, nex):
            self.val = val
            self.next = nex
    def __init__(self):
        self.head = None
    def getn(self, index: int) -> int:
        if index < 0:
            return -1
        i = 0
        n = self.head
        while n != None and i != index:
            n = n.next
            i += 1
        if i != index:
            return -1
        if n == None:
            return -1
        return n
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        i = 0
        n = self.head
        while n != None and i != index:
            n = n.next
            i += 1
        if i != index:
            return -1
        if n == None:
            return -1
        return n.val

    def addAtHead(self, val: int) -> None:
        n = self.Node(val, self.head)
        self.head = n

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            addAtHead(val)
            return
        prev = None
        n = self.head
        while n != None:
            prev = n
            n = n.next
        prev.next = self.Node(val,None)
        return
        


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            addAtHead(val)
            return
        prev = self.getn(index - 1)
        if prev == -1:
            return
        n = self.Node(val, prev.next)
        prev.next = n
        return


    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return
        prev = self.getn(index - 1)
        if prev == -1:
            return
        prevnext = prev.next
        if prevnext == None:
            return
        prev.next = prevnext.next
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)