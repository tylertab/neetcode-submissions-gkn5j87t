class DLLNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_from_dll(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_front(self,node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove_from_dll(node)
            self._add_to_front(node)
            return node.value
        return -1

    def _remove_lru(self):
        lru_node = self.tail.prev
        lru_node.prev.next = self.tail
        self.tail.prev = lru_node.prev
        del self.cache[lru_node.key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove_from_dll(node)
            node.value = value
            self._add_to_front(node)
            return
        if self.capacity == len(self.cache):
            self._remove_lru()
        new_node = DLLNode(key,value)
        self.cache[key] = new_node
        self._add_to_front(new_node)


