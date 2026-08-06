class LRUCache:
    class dll:
        def __init__(self, key,val, prev, next):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.head = self.dll(None,None,None,None)
        self.tail = self.dll(None,None,self.head,None)
        self.head.next = self.tail
        self.hm = {}

    def get(self, key: int) -> int:
        n = self.hm.get(key,self.dll(None,-1,None,None))
        if n.val == -1:
            return -1
        else:
            n.prev.next = n.next
            n.next.prev = n.prev
            n.prev = self.head
            n.next = self.head.next
            n.prev.next = n
            n.next.prev = n
            return n.val

    def put(self, key: int, value: int) -> None:
        n = self.hm.get(key)
        if n is not None:              # update in place, no eviction
            n.val = value
            n.prev.next = n.next
            n.next.prev = n.prev
            n.prev = self.head
            n.next = self.head.next
            n.prev.next = n
            n.next.prev = n
            return
        if self.size == self.capacity:
            n = self.tail.prev
            n.prev.next = n.next
            n.next.prev = n.prev
            del self.hm[n.key]
            self.size -= 1
        
        n = self.dll(key, value, self.head, self.head.next)
        n.prev.next = n
        n.next.prev = n
        self.hm[key] = n
        self.size += 1
        

            
