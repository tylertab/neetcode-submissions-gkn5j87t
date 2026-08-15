"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        s = set()
        curr = q
        while curr != None:
            s.add(curr)
            curr = curr.parent
        curr = p
        while curr != None:
            if curr in s:
                return curr
            curr = curr.parent
        return 