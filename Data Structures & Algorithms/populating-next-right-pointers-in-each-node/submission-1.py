"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
        q = [root]
        
        while len(q) > 0:
            count = len(q)
            prev = None
            for _ in range(count):
                curr = q.pop(0)
                if curr.left != None: 
                    q.append(curr.left)
                    q.append(curr.right)
                if prev != None:
                    prev.next = curr
                prev = curr
        return root


            
                


