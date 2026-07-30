"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        curr = head
        d[None] = None
        while curr is not None:
            d[curr] = Node(curr.val,None,None)
            curr = curr.next
        curr = head
        if not curr:
            return None
        point = d[curr]
        point.random = d[curr.random]
        point.next = d[curr.next]
        while curr.next is not None:
            curr = curr.next
            d[curr].next = d[curr.next]
            d[curr].random = d[curr.random]
            
            
        return point 
            
            
         