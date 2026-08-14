"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(r):
            if r == 'Node' or r == None:
                return 

            for n in r.children:
                print(n.val)
                helper(n)
            res.append(r.val)
            
        helper(root)
        return res