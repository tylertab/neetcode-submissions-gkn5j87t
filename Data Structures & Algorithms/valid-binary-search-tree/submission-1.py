# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _in_order(self, root, traversal):
        if root == None:
            return
        self._in_order(root.left, traversal)
        traversal.append(root.val)
        self._in_order(root.right, traversal)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        traversal = []
        self._in_order(root, traversal)

        for i in range(len(traversal) - 1):
            if traversal[i] >= traversal[i + 1]:
                return False
        return True
        