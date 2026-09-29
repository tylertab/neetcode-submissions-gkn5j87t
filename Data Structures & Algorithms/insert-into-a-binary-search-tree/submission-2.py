# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        prev = None
        while curr != None:
            if curr.val == val:
                return root
            if curr.val > val:
                prev = curr
                curr = curr.left
            elif curr.val < val:
                prev = curr
                curr = curr.right
        if prev == None:
            return TreeNode(val)
        if prev.val > val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)        
        return root