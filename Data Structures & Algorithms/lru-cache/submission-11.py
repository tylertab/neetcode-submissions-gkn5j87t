class DLLNode:
    def __init__(self):
        self.prev = None
        self.next = None
        self.key = None
        self.val = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove_node_from_dll(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_node_to_front(self,new_front):
        new_front.prev = self.head
        new_front.next = self.head.next
        self.head.next.prev = new_front
        self.head.next = new_front
    
    def _del_lru(self):
        lru_node = self.tail.prev
        self._remove_node_from_dll(lru_node)
        del self.cache[lru_node.key]

    def get(self, key: int) -> int:
        cache = self.cache
        if key in cache:
            node = cache[key]
            self._remove_node_from_dll(node)
            self._add_node_to_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        cache = self.cache
        if key in cache:
            node = cache[key]
            self._remove_node_from_dll(node)
            node.val = value
            self._add_node_to_front(node)
            return
        
        if len(cache) == self.capacity:
            self._del_lru()
        
        new_node = DLLNode()
        new_node.key = key
        new_node.val = value
        cache[key] = new_node
        self._add_node_to_front(new_node)

        
