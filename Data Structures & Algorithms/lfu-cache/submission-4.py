class Node:
    __slots__ = ("key", "val", "freq", "prev", "next")

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    """Doubly linked list with dummy head/tail. head.next = most recently used."""

    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self.size -= 1

    def remove_lru(self):
        if self.size == 0:
            return None
        lru = self.tail.prev
        self.remove(lru)
        return lru


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_node = {}      # key -> Node
        self.freq_list = {}     # freq -> DLL of nodes with that freq

    def _touch(self, node):
        """Bump a node's frequency by 1 and move it to the front of the new freq bucket."""
        old_freq = node.freq
        self.freq_list[old_freq].remove(node)
        if self.freq_list[old_freq].size == 0:
            del self.freq_list[old_freq]
            if self.min_freq == old_freq:
                self.min_freq += 1

        node.freq += 1
        self.freq_list.setdefault(node.freq, DLL()).add_front(node)

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self._touch(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self._touch(node)
            return

        if self.size >= self.capacity:
            evict_list = self.freq_list[self.min_freq]
            lru = evict_list.remove_lru()
            del self.key_node[lru.key]
            self.size -= 1
            if evict_list.size == 0:
                del self.freq_list[self.min_freq]

        node = Node(key, value)
        self.key_node[key] = node
        self.freq_list.setdefault(1, DLL()).add_front(node)
        self.min_freq = 1
        self.size += 1